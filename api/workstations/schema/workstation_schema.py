from datetime import time
from uuid import UUID

from pydantic import BaseModel, Field

from core.db.models.workstations import WorkstationStatus, WorkstationTitle


class WorkstationCreateSchema(BaseModel):
    title: WorkstationTitle
    description: str
    start_time: time
    end_time: time


class WorkstationPatchSchema(BaseModel):
    id: UUID
    data: dict = Field(default_factory=dict)


class WorkstationSchema(BaseModel):
    id: UUID
    title: WorkstationTitle
    status: WorkstationStatus
    description: str
    start_time: time
    end_time: time


class WorkstationDeleteSchema(BaseModel):
    data: WorkstationSchema
    msg: str = Field(default="deleted")
