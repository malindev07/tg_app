from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Sequence
from uuid import UUID

from api.records.schema.record_schema import (
    RecordWithAssociationSchema,
)
from api.response import ValidationInfoSchema
from api.workstations.schema.workstation_schema import WorkstationSchema


@dataclass
class RecordValidator:
    MIN_REPAIR_TIME: timedelta = timedelta(minutes=30)
    validation_name: str = "Record Validation"

    @staticmethod
    async def _validate_start_end_time(
            start_time: datetime, end_time: datetime, workstation: WorkstationSchema
    ):
        start_dt_ws = datetime.combine(datetime.today(), workstation.start_time)
        end_dt_ws = datetime.combine(datetime.today(), workstation.end_time)

        if start_dt_ws <= start_time and end_time <= end_dt_ws:
            return {}
        elif start_dt_ws > start_time:
            return {"start_time": f"Станция начинает работу позже чем {start_time}"}
        elif end_time > end_dt_ws:
            return {"end_time": f"Станция заканчивает работу до  {end_time}"}

    async def _validate_record_time_distance(
            self, start_time: datetime, end_time: datetime
    ) -> dict[str, str]:

        if end_time - start_time >= self.MIN_REPAIR_TIME:
            return {}
        else:
            return {
                "record_time_distance": f"Минимальный слот {self.MIN_REPAIR_TIME} мин"
            }

    @staticmethod
    async def _validate_record_staff_slot(
            start_time: datetime,
            end_time: datetime,
        records: Sequence[RecordWithAssociationSchema],
    ) -> dict[UUID, str]:
        
        # Проверка пересечения временных интервалов мастера(если пересекается то {........}, если нет {})
        for record in records:
            start_dt = datetime.combine(datetime.today(), record.start_time)
            end_dt = datetime.combine(datetime.today(), record.end_time)
            if (start_time < end_dt) and (end_time > start_dt):

                return {
                    record.staff_id: f"Мастер занят с {record.start_time} до {record.end_time}"
                }

        return {}

    async def is_validate(
        self,
            start_time: datetime,
            end_time: datetime,
        records: Sequence[RecordWithAssociationSchema],
            workstation: WorkstationSchema,
    ) -> ValidationInfoSchema:
        validate_record_time_distance = await self._validate_record_time_distance(
            start_time, end_time
        )
        validate_record_slot = await self._validate_record_staff_slot(
            start_time, end_time, records
        )
        validate_st_end_time_ws = await self._validate_start_end_time(
            start_time = start_time, end_time = end_time, workstation = workstation
        )

        validation_info = ValidationInfoSchema()
        validation_info.name = self.validation_name

        if validate_record_time_distance:
            validation_info.data.append(validate_record_time_distance)
        if validate_record_slot:
            validation_info.data.append(validate_record_slot)
        if validate_st_end_time_ws:
            validation_info.data.append(validate_st_end_time_ws)

        return validation_info
