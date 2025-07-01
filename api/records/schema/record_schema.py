from datetime import time, date
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

from core.db.models import RecordStatus


class RecordCreateSchema(BaseModel):
    car_id: UUID
    staff_id: UUID
    workstation_id: UUID
    reason: str
    comment: str
    record_date: date
    start_time: str | time
    end_time: str | time

    @field_validator("start_time", "end_time")
    def validate_time_format(cls, v):
        try:
            # Преобразуем строку "HH:MM" в объект time
            hours, minutes = map(int, v.split(":"))
            return time(hour=hours, minute=minutes)
        except ValueError:
            raise ValueError("Неверный форматы времени. Используйте ЧЧ:ММ")


class RecordPatchSchema(BaseModel):
    id: UUID
    data: dict[str, str] = Field(default={})


class RecordWithStaffSchema(BaseModel):
    id: UUID
    car_id: UUID
    staff_id: UUID | list[UUID]
    reason: str
    status: RecordStatus
    comment: str
    record_date: date
    start_time: time
    end_time: time


class RecordWithAssociationSchema(BaseModel):
    id: UUID
    workstation_id: UUID
    car_id: UUID
    staff_id: UUID | list[UUID]
    reason: str
    status: RecordStatus
    comment: str
    record_date: date
    start_time: time
    end_time: time


class RecordSchema(BaseModel):
    id: UUID
    car_id: UUID
    reason: str
    status: RecordStatus
    comment: str
    record_date: date
    start_time: time
    end_time: time


class RecordDeleteSchema(BaseModel):
    data: RecordSchema
    msg: str = Field(default="deleted")
