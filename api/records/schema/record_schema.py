from datetime import time, date
from uuid import UUID

from pydantic import BaseModel, Field

from core.db.models import RecordStatus


class RecordCreateSchema(BaseModel):
    client_id: UUID
    car_id: UUID
    staff_id: list[UUID]
    workstation_id: UUID
    reason: str
    comment: str
    record_date: date
    start_time: time
    end_time: time


class RecordPatchSchema(BaseModel):
    id: UUID
    data: dict[str, str] = Field(default={})


class RecordWithStaffSchema(BaseModel):
    id: UUID
    client_id: UUID
    car_id: UUID
    staff_id: list[UUID]
    reason: str
    status: RecordStatus
    comment: str
    record_date: date
    start_time: time
    end_time: time


class RecordWithAssociationSchema(BaseModel):
    id: UUID
    workstation_id: UUID
    client_id: UUID
    car_id: UUID
    staff_id: list[UUID]
    reason: str
    status: RecordStatus
    comment: str
    record_date: date
    start_time: time
    end_time: time


class RecordSchema(BaseModel):
    id: UUID
    client_id: UUID
    car_id: UUID
    # staff_id: UUID
    reason: str
    status: RecordStatus
    comment: str
    record_date: date
    start_time: time
    end_time: time
    # created_at: datetime
    # updated_at: datetime


class RecordDeleteSchema(BaseModel):
    data: RecordSchema
    msg: str = Field(default="deleted")
