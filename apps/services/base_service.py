from abc import ABC, abstractmethod
from dataclasses import dataclass

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
        session: AsyncSession,
    ) -> SchemaType: ...

    @abstractmethod
    async def get(self, attr) -> SchemaType: ...

    @abstractmethod
    async def update(self, attr) -> SchemaType: ...

    @abstractmethod
    async def delete(self, attr) -> SchemaType: ...

    @abstractmethod
    async def get_by_name(self, attr) -> SchemaType: ...

    @abstractmethod
    def _to_schema(self, obj: MODEL) -> SCHEMA:
        """Конвертирует модель в схему"""
        return self.SCHEMA.model_validate(obj, from_attributes=True)

    @abstractmethod
    def _to_model(self, data: SCHEMA) -> MODEL:
        """Конвертирует схему в модель"""
        return self.MODEL._model(**data.model_dump())
