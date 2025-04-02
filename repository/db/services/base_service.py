from abc import ABC, abstractmethod
from dataclasses import dataclass

from repository.db.generics import ModelType


@dataclass
class BaseService(ABC):

    @abstractmethod
    async def create(self, attr) -> ModelType: ...

    @abstractmethod
    async def get(self, attr) -> ModelType: ...

    @abstractmethod
    async def update(self, attr) -> ModelType: ...

    @abstractmethod
    async def delete(self, attr) -> ModelType: ...

    @abstractmethod
    async def get_by_name(self, attr) -> ModelType: ...
