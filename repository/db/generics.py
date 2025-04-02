from typing import TypeVar

from repository.db.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)
