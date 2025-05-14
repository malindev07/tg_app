import re
from dataclasses import dataclass

from api.cars.schemas.schema import CarValidationInfoSchema


@dataclass
class CarValidator:

    @staticmethod
    def _validate_gos_nomer(gos_nomer: str) -> dict[str, str]:
        match = re.fullmatch(r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}", gos_nomer)
        if match:
            return {}
        else:

            return {gos_nomer: "Incorrect value"}

    @staticmethod
    def _validate_vin(vin: str) -> dict[str, str]:
        if len(vin) == 17:
            return {}
        else:

            return {vin: "Incorrect value"}

    def is_validate(self, vin: str, gos_nomer: str) -> CarValidationInfoSchema:
        validate_gos_nomer = self._validate_gos_nomer(gos_nomer)
        validate_vin = self._validate_vin(vin)
        incorrect_values = CarValidationInfoSchema()

        if validate_vin:
            incorrect_values.data.append(validate_vin)
        if validate_gos_nomer:
            incorrect_values.data.append(validate_gos_nomer)

        return incorrect_values
