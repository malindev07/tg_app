from typing import Optional

from pydantic import BaseModel, Field


class CarIDApi(BaseModel):
    car_id: str


class CarCreateAPI(BaseModel):
    car_id: str
    car_brand: str
    car_model: str
    car_owner: int
    car_vin: str


class CarNewIdOwnerAPI(BaseModel):
    id: str | None = None
    owner: int | None = None


class CarReturnAPI(BaseModel):
    car_id: str | None
    car_brand: str | None
    car_model: str | None
    car_owner: int | None
    car_vin: str | None
