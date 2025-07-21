from typing import Optional, Any
from uuid import UUID

from pydantic import BaseModel, Field

from api.cars.schema import CarSchema


class CustomerCreateSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    phone: str


class CustomerPatchSchema(BaseModel):
    id: UUID
    data: dict[str, Any] = Field(default_factory=dict)


class CustomerValidateErrorPhoneSchema(BaseModel):
    data: str
    msg: str


class CustomerAlreadyExistsSchema(BaseModel):
    data: str
    msg: str


class CustomerCarsSchema(BaseModel):
    cars: list[CarSchema] = Field(default_factory=list)


class CustomerSchema(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: str | None = None
    phone: str
    is_verify: bool = False
    tg_id: str | None = None
    discount: int = 0


class CustomerDeleteSchema(BaseModel):
    data: CustomerSchema
    msg: str = Field(default="deleted")
