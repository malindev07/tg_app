from typing import Optional, Any
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

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
    gos_nomer: str = Field(
        description="Госномер автомобиля", examples=["А111АА11", "С867ХЕ790"]
    )
    brand: str = Field(description="Марка автомобиля", examples=["BMW", "KIA"])
    model: str = Field(description="Модель автомобиля", examples=["X3", "RIO"])
    vin: str | None = Field(
        default=None,
        description="VIN автомобиля из 17 символов",
        examples=["XWET1234ERT345678"],
    )
    odometer_registered: int = Field(
        description="Пробег автомобиля", examples=["193000", "1000"]
    )
    odometer_last: int | None = None
    owner_id: UUID

    @field_validator("gos_nomer")
    def validate_time_format(cls, plate):
        return "".join(TRANSLIT_MAP.get(letter, letter) for letter in plate)


class CarGetByFieldSchema(BaseModel):
    key: str
    value: str


class CarAlreadyExistsSchema(BaseModel):
    data: str
    msg: str = Field(default="Already exists")


class CarPatchSchema(BaseModel):
    id: UUID
    data: dict[str, Any] = Field(default_factory=dict)


class CarSchema(BaseModel):
    id: Optional[UUID]
    gos_nomer: str
    brand: str
    model: str
    vin: str | None = None
    odometer_registered: int
    odometer_last: int


class CarDeletedSchema(BaseModel):
    data: CarSchema
    msg: str = Field(default="deleted")
