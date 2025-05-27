from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Any
from uuid import UUID

from core.db.generics import ModelType, SchemaType
from repository.base_repository import RepositoryORM


@dataclass
class BaseServices(ABC, Generic[ModelType, SchemaType]):

    MODEL = ModelType
    SCHEMA = SchemaType
    repository: RepositoryORM

    @abstractmethod
    async def create(self, model: SchemaType) -> SchemaType: ...

    @abstractmethod
    async def get(self, id_: UUID) -> ModelType | None: ...

    @abstractmethod
    async def delete(self, id_: UUID) -> ModelType | None: ...

    @abstractmethod
    async def get_by_field(self, key: str, value: str) -> ModelType | None: ...


@dataclass
class MainServices(BaseServices, Generic[ModelType, SchemaType]):

    MODEL = ModelType
    SCHEMA = SchemaType
    repository: RepositoryORM

    async def create(self, model: MODEL) -> MODEL:
        obj = await self.repository.create(model=model)
        return obj

    async def get(self, id_: UUID) -> MODEL | None:
        return await self.repository.get(id_=id_)

    async def get_by_field(self, key: str, value: str) -> MODEL | None:
        return await self.repository.get_by_field(key=key, value=value)

    async def delete(self, id_: UUID) -> MODEL | None:
        obj = await self.repository.get(id_=id_)
        if obj:
            await self.repository.delete(model=obj)
        return obj

    async def patch(self, id_: UUID, data: dict[str, Any]) -> MODEL:
        return await self.repository.patch(id_=id_, data=data)
