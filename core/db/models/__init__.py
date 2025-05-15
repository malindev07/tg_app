from core.db.models.base import Base
from core.db.models.cars import CarModel

__all__ = ["Base", "CarModel", "CustomerModel"]

from core.db.models.customers import CustomerModel
