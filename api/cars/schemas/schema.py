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


class CarSchema(BaseModel):
    id: UUID
    gos_nomer: str
    brand: str
    model: str
    vin: Optional[str] = Field(default=None)
    # Новый способ конфигурации в Pydantic v2
    model_config = ConfigDict(
        from_attributes=True,  # Замена orm_mode=True
        populate_by_name=True,  # Если нужно alias-преобразование
    )
