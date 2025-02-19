from dataclasses import dataclass
import re


@dataclass
class CarValidator:

    @staticmethod
    def validate_car_id(car_id: str) -> bool:
        match = re.fullmatch(r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}", car_id)
        if match:
            print(car_id, "validate successful")
            return True
        else:
            print(car_id, "validate error")
            return False

    @staticmethod
    def validate_car_vin(car_vin: str) -> bool:
        if len(car_vin) == 17:
            print(car_vin, "validate successful")
            return True
        else:
            print(car_vin, "validate error")
            return False
