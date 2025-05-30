from dataclasses import dataclass
from datetime import time, datetime, timedelta
from typing import Sequence

from api.records.schema.record_schema import RecordWithAssociationSchema


@dataclass
class RecordValidator:
    MIN_REPAIR_TIME: timedelta = timedelta(minutes = 30)

    def validate_record_time_distance(self, start_time: time, end_time: time) -> bool:
        start_dt = datetime.combine(datetime.today(), start_time)
        end_dt = datetime.combine(datetime.today(), end_time)
        return end_dt - start_dt >= self.MIN_REPAIR_TIME

    def validate_record_slot(
            self,
            start_time: time,
            end_time: time,
            records: Sequence[RecordWithAssociationSchema],
    ) -> RecordWithAssociationSchema | bool:
        start_dt_new = datetime.combine(datetime.today(), start_time)
        end_dt_new = datetime.combine(datetime.today(), end_time)
        
        # Проверка пересечения временных интервалов (если пересекается то True, если нет False)
        for record in records:
            start_dt = datetime.combine(datetime.today(), record.start_time)
            end_dt = datetime.combine(datetime.today(), record.end_time)
            if (start_dt_new < end_dt) and (end_dt_new > start_dt):
                return record
        
        return False
