from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class CreateCustomerSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = Field(default = None)
    phone: str


class CustomerSchema(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: str = Field(default = str)
    phone: str
    is_verify: bool = Field(default = False)
    tg_id: str = Field(default = False)
    discount: int = Field(default = 0)
