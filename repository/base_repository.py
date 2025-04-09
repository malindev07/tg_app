from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.generics import ModelType


@dataclass
class RepositoryBase(ABC):
    MODEL = ModelType

    @abstractmethod
    async def create(self, session: AsyncSession, model: type[MODEL]) -> MODEL: ...

    @abstractmethod
    async def get(self, session: AsyncSession, id_: UUID) -> MODEL: ...

    @abstractmethod
    async def delete(self, session: AsyncSession, id_: UUID) -> MODEL: ...

    @abstractmethod
    async def get_by_field(
        self,
        key: str,
        value: str,
        session: AsyncSession,
    ) -> MODEL | None: ...


@dataclass
class RepositoryORM(RepositoryBase):
    MODEL = ModelType

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

    async def delete(self, session: AsyncSession, model: MODEL) -> None:
        await session.delete(model)
        await session.commit()

    async def get_by_field(
        self,
        key: str,
        value: str,
        session: AsyncSession,
    ) -> MODEL | None:
        query = select(self.MODEL).where(getattr(self.MODEL, key) == value)
        result = await session.execute(query)
        obj = result.scalar_one_or_none()
        return obj
