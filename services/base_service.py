from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Type
from uuid import UUID


from sqlalchemy.ext.asyncio import AsyncSession

from core.db.generics import ModelType, SchemaType
from repository.base_repository import RepositoryBase, RepositoryORM


@dataclass
class BaseServices(ABC, Generic[ModelType, SchemaType]):

    MODEL = ModelType
    SCHEMA = SchemaType
    repository: RepositoryBase

    @abstractmethod
    async def create(self, model: SchemaType, session: AsyncSession) -> SchemaType: ...

    @abstractmethod
    async def get(self, id_: UUID, session: AsyncSession) -> MODEL | None: ...

    @abstractmethod
    async def delete(
        self, id_: UUID, session: AsyncSession
    ) -> dict[UUID, str] | None: ...

    @abstractmethod
    def _to_schema(self, obj: ModelType) -> SchemaType: ...

    @abstractmethod
    def _to_model(self, data: SchemaType) -> ModelType: ...


@dataclass
class MainServices(BaseServices, Generic[ModelType, SchemaType]):

    MODEL = ModelType
    SCHEMA = SchemaType
    repository: RepositoryORM

    async def create(self, schema: SCHEMA, session: AsyncSession) -> SCHEMA:
        model = await self._to_model(schema)  # из pydantic схемы в модель
        obj = await self.repository.create(model=model, session=session)
        return await self._to_schema(obj)  # из модели в схему pydantic

    async def get(self, id_: UUID, session: AsyncSession) -> MODEL | None:
        return await self.repository.get(id_=id_, session=session)

    async def delete(self, id_: UUID, session: AsyncSession) -> dict[UUID, str] | None:
        # obj = await self.get(id_=id_, session=session) TODO уточнить!
        obj = await self.repository.get(id_=id_, session=session)
        if obj:
            await self.repository.delete(session=session, model=obj)
            return {id_: "deleted"}  # Уточнить как правильно сделать

        return None

    async def get_by_field(
        self, key: str, value: str, session: AsyncSession
    ) -> MODEL | None:
        return await self.repository.get_by_field(key=key, value=value, session=session)

    async def _to_schema(self, obj: MODEL) -> SCHEMA:
        """Конвертирует модель в схему"""
        return self.SCHEMA.model_validate(obj, from_attributes=True)

    async def _to_model(self, schema: SCHEMA) -> MODEL:
        """Конвертирует схему в модель"""
        return self.MODEL(**schema.model_dump())
