from uuid import UUID
from dataclasses import dataclass
from core.db.models import CarModel
from sqlalchemy.ext.asyncio import AsyncSession
from repository.car_repository.repository import CarRepository
from services.base_service import MainServices
from api.cars.schemas.schema import (
    CarCreateSchema,
    CarSchema,
    CarAlreadyExistsSchema,
    CarValidationInfoSchema,
)
from services.car_services.validator.car_validator import CarValidator


@dataclass
class CarServices(MainServices[CarModel, CarSchema]):
    MODEL = CarModel
    SCHEMA = CarSchema
    repository: CarRepository
    validator: CarValidator

    async def create(
        self, schema: CarCreateSchema, session: AsyncSession
    ) -> SCHEMA | CarAlreadyExistsSchema | CarValidationInfoSchema:

        validation_res: CarValidationInfoSchema = self.validator.is_validate(
            vin=schema.vin,
            gos_nomer=schema.gos_nomer,
        )

        if validation_res.data:
            return validation_res

        obj = await super().get_by_field(
            key="gos_nomer", value=schema.gos_nomer, session=session
        )
        if obj:
            return CarAlreadyExistsSchema(data=schema.gos_nomer)

        return await super().create(schema=schema, session=session)

    async def get(self, id_: UUID, session: AsyncSession) -> SCHEMA | None:
        return await super()._to_schema(
            await super().get(id_=id_, session=session),
        )

    async def delete(self, id_: UUID, session: AsyncSession) -> dict[UUID, str] | None:
        return await super().delete(id_, session)
