import re
from dataclasses import dataclass

from api.response import ValidationInfoSchema


@dataclass
class StaffValidator:
    validation_name: str = "Staff Validation"

    @staticmethod
    async def _validate_phone(phone: str) -> dict[str, str]:
        match = re.fullmatch(r"[+7|8]\d{10}", phone)
        if match:
            return {}
        else:
            return {phone: "Incorrect phone"}

    async def is_validate(self, phone: str) -> ValidationInfoSchema:
        validate_phone = await self._validate_phone(phone)

        validation_info = ValidationInfoSchema()
        validation_info.name = self.validation_name

        if validate_phone:
            validation_info.data.append(validate_phone)

        return validation_info
