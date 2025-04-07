from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from api.cars.schemas.schema import CarCreateSchema, CarSchema
from apps.services.base_service import BaseService
from core.db.generics import SchemaType
from core.db.models import CarModel
from repository.car_repository.repository import CarRepository, get_car_repo


@dataclass
class CarServices(BaseService):
    MODEL = CarModel
    SCHEMA = CarSchema
    repository: CarRepository

    async def create(
        self,
        schema: CarCreateSchema,
        session: AsyncSession,
    ) -> SchemaType:
        model = await super()._to_model(schema)  # из pydantic схемы в модель
        obj = await self.repository.create(session=session, model=model)
        return await super()._to_schema(obj)  # из модели в схему pydantic


car_service = CarServices(repository=await get_car_repo())


async def get_car_services() -> CarServices:
    return CarServices()
