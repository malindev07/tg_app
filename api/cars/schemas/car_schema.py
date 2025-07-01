from typing import Optional, Any
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict, field_validator

TRANSLIT_MAP = {
    "А": "A",
    "В": "B",
    "Е": "E",
    "К": "K",
    "М": "M",
    "Н": "H",
    "О": "O",
    "Р": "P",
    "С": "C",
    "Т": "T",
    "У": "Y",
    "Х": "X",
}


class CarCreateSchema(BaseModel):
    gos_nomer: str
    brand: str
    model: str
    vin: Optional[str] | None = None
    odometer_registered: int
    odometer_last: Optional[int] | None = None
    owner_id: UUID

    @field_validator("gos_nomer")
    def validate_time_format(cls, plate):
        return "".join(TRANSLIT_MAP.get(letter, letter) for letter in plate)


class CarGetByFieldSchema(BaseModel):
    key: str
    value: str


class CarValidationInfoSchema(BaseModel):
    data: list[dict[Any, Any]] = Field(default=[])


class CarAlreadyExistsSchema(BaseModel):
    data: str
    msg: str = Field(default="Already exists")


class CarPatchSchema(BaseModel):
    id: UUID
    data: dict[Any, Any] = Field(default={})


class CarSchema(BaseModel):
    id: Optional[UUID]
    gos_nomer: str
    brand: str
    model: str
    vin: Optional[str] = Field(default=None)
    odometer_registered: int
    odometer_last: int

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class CarDeletedSchema(BaseModel):
    data: CarSchema
    msg: str = Field(default="deleted")
