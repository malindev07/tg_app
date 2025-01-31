from dataclasses import dataclass
import re


@dataclass
class CarValidator:

    @staticmethod
    def validate_car_id(car_id: str):
        match = re.fullmatch(r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}", car_id)
        return True if match else False

    @staticmethod
    def validate_car_vin(car_vin: str):
        return True if len(car_vin) == 17 else False
