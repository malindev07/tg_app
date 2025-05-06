from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class CarIDSchema(BaseModel):
    id_: UUID


class CarCreateSchema(BaseModel):
    gos_nomer: str
    brand: str
    model: str
    vin: Optional[str] | None = None


class CarNewIdOwnerAPI(BaseModel):
    id: str | None = None
    owner: int | None = None


class CarGetByFieldSchema(BaseModel):
    key: str
    value: str


class CarValidationInfoSchema(BaseModel):
    data: list = Field(default_factory=list)


class CarAlreadyExistsSchema(BaseModel):
    data: str
    msg: str = Field(default="Already exists")


class CarPatchSchema(BaseModel):
    id: UUID
    data: dict = Field(default_factory=dict)


class CarSchema(BaseModel):
    id: Optional[UUID]
    gos_nomer: str
    brand: str
    model: str
    vin: Optional[str] = Field(default=None)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class CarDeletedSchema(BaseModel):
    data: CarSchema
    msg: str = Field(default="deleted")
