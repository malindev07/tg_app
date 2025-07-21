from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from core.db.models.staff import StaffStatus, StaffPosition


class StaffCreateSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    position: StaffPosition = Field(
        default=StaffPosition.JUNIOR_MASTER,
        description="""
            SENIOR_MASTER = "Старший мастер"
            MIDDLE_MASTER = "Мастер"
            JUNIOR_MASTER = "Младший мастер"
            TRAINEE = "Стажер"
    """,
    )
    phone: str
    salary_rate: float
    comment: str


class StaffPatchSchema(BaseModel):
    id: UUID
    data: dict[str, Any] = Field(default_factory=dict)


class StaffSchema(BaseModel):
    id: UUID
    position: StaffPosition
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    status: StaffStatus
    salary_rate: float
    comment: str


class StaffDeleteSchema(BaseModel):
    data: StaffSchema
    msg: str = Field(default="deleted")
