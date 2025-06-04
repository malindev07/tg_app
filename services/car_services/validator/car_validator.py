import re
from dataclasses import dataclass

from api.response import ValidationInfoSchema


@dataclass
class CarValidator:
    name: str = "Car Validation"

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

    def is_validate(self, vin: str, gos_nomer: str) -> ValidationInfoSchema:
        validate_gos_nomer = self._validate_gos_nomer(gos_nomer)
        validate_vin = self._validate_vin(vin)
        validation_info = ValidationInfoSchema()
        validation_info.name = self.name

        if validate_vin:
            validation_info.data.append(validate_vin)
        if validate_gos_nomer:
            validation_info.data.append(validate_gos_nomer)

        return validation_info
