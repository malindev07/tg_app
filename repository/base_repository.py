from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
from uuid import UUID


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from core.db.generics import ModelType
from core.db.helper import db_helper


@dataclass
class RepositoryBase(ABC):
    MODEL = ModelType
    session_factory: async_sessionmaker[AsyncSession] = db_helper.session_factory

    @abstractmethod
    async def create(self, model: MODEL) -> MODEL: ...

    @abstractmethod
    async def get(self, id_: UUID) -> MODEL: ...

    @abstractmethod
    async def get_by_field(self, key: str, value: str) -> MODEL | None: ...

    @abstractmethod
    async def delete(self, id_: UUID) -> MODEL: ...


@dataclass
class RepositoryORM(RepositoryBase):
    MODEL = ModelType
    session_factory = db_helper.session_factory

    async def create(self, model: MODEL) -> MODEL:
        try:
            async with self.session_factory() as session:
                session.add(model)
                await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        return model

    async def get(self, id_: UUID) -> MODEL | None:
        async with self.session_factory() as session:
            query = select(self.MODEL).where(self.MODEL.id == id_)
            res = await session.execute(query)
            obj = res.scalar_one_or_none()
            return obj

    async def get_by_field(self, key: str, value: str) -> MODEL | None:
        async with self.session_factory() as session:
            query = select(self.MODEL).where(getattr(self.MODEL, key) == value)
            result = await session.execute(query)
            obj = result.scalar_one_or_none()
            return obj

    async def delete(self, model: MODEL) -> None:
        async with self.session_factory() as session:
            await session.delete(model)
            await session.commit()

    async def patch(self, id_: UUID, data: dict[str, Any]) -> MODEL:
        async with self.session_factory() as session:
            query = select(self.MODEL).where(self.MODEL.id == id_)
            res = await session.execute(query)
            model = res.scalar_one_or_none()
            for field, value in data.items():
                if hasattr(model, field):
                    setattr(model, field, value)
            await session.commit()
            await session.refresh(model)
            return model
