import re
from dataclasses import dataclass


@dataclass
class CustomerValidator:
    
    async def validate_phone(self, phone: str) -> bool:
        match = re.fullmatch(r"[+7|8]\d{10}", phone)
        if match:
            return True
        else:
            return False
