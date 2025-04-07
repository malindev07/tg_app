from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.generics import SchemaType, ModelType


@dataclass
class RepositoryBase(ABC):
    MODEL = ModelType

    @abstractmethod
    async def create(self, session: AsyncSession, model: type[MODEL]) -> MODEL: ...
    @abstractmethod
    async def get(self, session: AsyncSession, id_: UUID) -> MODEL: ...


@dataclass
class RepositoryORM(RepositoryBase):
    MODEL = ModelType
    SCHEMA = SchemaType

    async def create(self, session: AsyncSession, model: type[MODEL]) -> MODEL:
        try:
            session.add(model)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        return model

    async def get(self, session: AsyncSession, id_: UUID) -> MODEL | None:
        query = select(self.MODEL).where(self.MODEL.id == id_)
        res = await session.execute(query)
        obj = res.scalar_one_or_none()
        return obj
