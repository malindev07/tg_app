from dataclasses import dataclass
from typing import Optional


# from vininfo import Vin


@dataclass(slots=True)
class CarId:
    car_id: str


@dataclass(slots=True, frozen=True)
class CarBrandModel:
    car_brand: str
    car_model: str


@dataclass(slots=True, frozen=True)
class CarVIN:
    car_vin: str


@dataclass(slots=True)
class Car:
    car_id: CarId
    car_brand: str
    car_model: str
    car_owner: int
    car_vin: CarVIN


# vin = Vin("WBAWX710500B98068")
# print(vin.brand)
# print(vin.years)
# print(vin.annotate())
