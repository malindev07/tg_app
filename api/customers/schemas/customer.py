from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class CustomerCreateSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = Field(default=None)
    phone: str


class CustomerPatchSchema(BaseModel):
    id: UUID
    data: dict = Field(default_factory=dict)


class CustomerValidateErrorPhoneSchema(BaseModel):
    data: str
    msg: str


class CustomerAlreadyExistsSchema(BaseModel):
    data: str
    msg: str


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
