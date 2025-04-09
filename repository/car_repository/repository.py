from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.models import CarModel
from repository.base_repository import RepositoryORM


@dataclass
class CarRepository(RepositoryORM):
    MODEL = CarModel

    async def create(
        self,
        model: MODEL,
        session: AsyncSession,
    ) -> MODEL:
        return await super().create(session=session, model=model)

    async def get(
        self,
        id_: UUID,
        session: AsyncSession,
    ) -> MODEL:
        return await super().get(session=session, id_=id_)
