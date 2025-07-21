from datetime import time
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

from core.db.models.workstations import WorkstationStatus, WorkstationTitle


class WorkstationCreateSchema(BaseModel):
    title: WorkstationTitle
    post_number: int
    description: str
    start_time: str
    end_time: str

    @field_validator("start_time", "end_time")
    def validate_time_format(cls, v):
        try:
            # Преобразуем строку "HH:MM" в объект time
            hours, minutes = map(int, v.split(":"))
            return time(hour=hours, minute=minutes)
        except ValueError:
            raise ValueError("Неверный форматы времени. Используйте ЧЧ:ММ")


# todo Уточнить у Артема ( например, "post_number":1" )
class WorkstationPatchSchema(BaseModel):
    id: UUID
    data: dict[str, Any] = Field(default_factory=dict)


class WorkstationSchema(BaseModel):
    id: UUID
    title: WorkstationTitle
    post_number: int
    status: WorkstationStatus
    description: str
    start_time: time
    end_time: time


class WorkstationDeleteSchema(BaseModel):
    data: WorkstationSchema
    msg: str = Field(default="deleted")
