from dataclasses import dataclass, field
import re


@dataclass
class CarValidator:
    car_vin: str
    car_id: str

    def _validate_car_id(self, car_id: str) -> bool:
        match = re.fullmatch(r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}", car_id)
        if match:
            print(car_id, "validate successful")
            return True
        else:
            print(car_id, "validate error")
            return False

    def _validate_car_vin(self, car_vin: str) -> bool | ValueError:
        if len(car_vin) == 17:
            print(car_vin, "validate successful")
            return True
        else:
            print(car_vin, "validate error")
            raise ValueError

    def is_validate(self) -> bool:
        res = self._validate_car_vin(self.car_vin) and self._validate_car_id(
            self.car_id
        )
        return res
