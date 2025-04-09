from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import AsyncGenerator
from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.cars.schemas.schema import CarSchema, CarCreateSchema, CarIDSchema
from core.db.helper import db_helper
from core.db.models import CarModel
from repository.base_repository import RepositoryORM


@dataclass
class CarRepository(RepositoryORM):
    MODEL = CarModel
    SCHEMA = CarSchema  # Основная схема

    async def create(
        self, model: MODEL, session: AsyncSession = Depends(db_helper.session)
    ) -> MODEL:
        return await super().create(session, model)

    async def get(
        self, id_: UUID, session: AsyncSession = Depends(db_helper.session)
    ) -> MODEL:
        print(session)
        print(type(session))
        return await super().get(session, id_)

    # async def _to_model(self, data: SCHEMA) -> MODEL:
    #     model_data = data.model_dump()
    #     return self.MODEL(**model_data)
    #
    # async def _to_schema(self, obj: MODEL) -> SCHEMA:
    #     return self.SCHEMA.model_validate(obj)


# @asynccontextmanager
# async def get_car_repo(
#     session: AsyncSession = Depends(db_helper.session),
# ) -> AsyncGenerator[CarRepository, None]:
#     yield CarRepository(session=session)
