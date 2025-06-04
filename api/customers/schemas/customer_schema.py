from typing import Optional, Any
from uuid import UUID

from pydantic import BaseModel, Field

from api.cars.schemas.car_schema import CarSchema


class CustomerCreateSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = Field(default=None)
    phone: str


class CustomerPatchSchema(BaseModel):
    id: UUID
    data: dict[Any, Any] = Field(default={})


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
    middle_name: Optional[str] = Field(default=None)
    phone: str
    is_verify: bool = Field(default=False)
    tg_id: Optional[str] = Field(default=None)
    discount: int = Field(default=0)


class CustomerDeleteSchema(BaseModel):
    data: CustomerSchema
    msg: str = Field(default="deleted")
