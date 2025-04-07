from dataclasses import dataclass
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from api.cars.schemas.schema import CarSchema, CarCreateSchema, CarIDSchema
from core.db.models import CarModel
from repository.base_repository import RepositoryORM


@dataclass
class CarRepository(RepositoryORM):
    MODEL = CarModel
    SCHEMA = CarSchema  # Основная схема

    async def create(self, session: AsyncSession, model: MODEL) -> MODEL:
        return await super().create(session, model)

    async def get(self, session: AsyncSession, id_: UUID) -> MODEL:
        return await super().get(session, id_)

    async def _to_model(self, data: SCHEMA) -> MODEL:
        model_data = data.model_dump()
        return self.MODEL(**model_data)

    async def _to_schema(self, obj: MODEL) -> SCHEMA:
        return self.SCHEMA.model_validate(obj)


car_repo = CarRepository()


async def get_car_repo() -> CarRepository:
    return car_repo
