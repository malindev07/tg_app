from dataclasses import dataclass
from typing import Optional


@dataclass
class CarCreate:
    car_id: str
    car_brand: str
    car_model: str
    car_owner: str
    car_vin: Optional[str]
