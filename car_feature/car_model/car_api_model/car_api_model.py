from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class CarCreateAPI(BaseModel):
    car_id: str
    car_brand: str
    car_model: str
    car_owner: str
    car_vin: str


@dataclass
class CarReturnAPI:
    car_id: str
    car_brand: str
    car_model: str
    car_owner: str
