from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from core.db.generics import ModelType, SchemaType
from repository.base_repository import RepositoryBase


@dataclass
class BaseService(ABC):
    MODEL = ModelType
    SCHEMA = SchemaType

    @abstractmethod
    async def create(
        self,
        model: type[MODEL],
        # session: AsyncSession,
    ) -> SchemaType: ...

    @abstractmethod
    async def get(
        self,
        id_: UUID,
        # session: AsyncSession,
    ) -> SchemaType: ...

    # @abstractmethod
    # async def update(self, attr) -> SchemaType: ...
    #
    # @abstractmethod
    # async def delete(self, attr) -> SchemaType: ...
    #
    # @abstractmethod
    # async def get_by_name(self, attr) -> SchemaType: ...

    @abstractmethod
    def _to_schema(self, obj: MODEL) -> SCHEMA: ...

    @abstractmethod
    def _to_model(self, data: SCHEMA) -> MODEL: ...
