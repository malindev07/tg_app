from dataclasses import dataclass
from datetime import time, datetime, timedelta
from typing import Sequence
from uuid import UUID

from api.records.schema.record_schema import (
    RecordWithAssociationSchema,
)
from api.response import ValidationInfoSchema


@dataclass
class RecordValidator:
    MIN_REPAIR_TIME: timedelta = timedelta(minutes=30)
    validation_name: str = "Record Validation"

    async def _validate_record_time_distance(
        self, start_time: time, end_time: time
    ) -> dict[str, str]:
        start_dt = datetime.combine(datetime.today(), start_time)
        end_dt = datetime.combine(datetime.today(), end_time)

        if end_dt - start_dt >= self.MIN_REPAIR_TIME:
            return {}
        else:
            return {
                "record_time_distance": f"Минимальный слот {self.MIN_REPAIR_TIME} мин"
            }

    @staticmethod
    async def _validate_record_slot(
        start_time: time,
        end_time: time,
        records: Sequence[RecordWithAssociationSchema],
    ) -> dict[UUID, str]:
        start_dt_new = datetime.combine(datetime.today(), start_time)
        end_dt_new = datetime.combine(datetime.today(), end_time)

        # Проверка пересечения временных интервалов (если пересекается то {........}, если нет {})
        for record in records:
            start_dt = datetime.combine(datetime.today(), record.start_time)
            end_dt = datetime.combine(datetime.today(), record.end_time)
            if (start_dt_new < end_dt) and (end_dt_new > start_dt):

                return {
                    record.id: f"Время с {record.start_time} до {record.end_time} занято"
                }

        return {}

    async def is_validate(
        self,
        start_time: time,
        end_time: time,
        records: Sequence[RecordWithAssociationSchema],
    ) -> ValidationInfoSchema:
        validate_record_time_distance = await self._validate_record_time_distance(
            start_time, end_time
        )
        validate_record_slot = await self._validate_record_slot(
            start_time, end_time, records
        )

        validation_info = ValidationInfoSchema()
        validation_info.name = self.validation_name

        if validate_record_time_distance:
            validation_info.data.append(validate_record_time_distance)
        if validate_record_slot:
            validation_info.data.append(validate_record_slot)

        return validation_info
