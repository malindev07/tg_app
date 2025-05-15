from datetime import datetime, time, date
from uuid import UUID

from pydantic import BaseModel

from core.db.models import RecordStatus


class RecordCreateSchema(BaseModel):
    client_id: UUID
    car_id: UUID
    reason: str
    comment: str
    record_date: date
    start_time: time
    end_time: time


class RecordSchema(BaseModel):
    id: UUID
    client_id: UUID
    car_id: UUID
    reason: str
    status: RecordStatus
    comment: str
    record_date: date
    start_time: time
    end_time: time
    created_at: datetime
    updated_at: datetime
