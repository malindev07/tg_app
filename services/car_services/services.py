from dataclasses import dataclass
from uuid import UUID

from api.cars.schemas.car_schema import (
    CarCreateSchema,
    CarSchema,
    CarAlreadyExistsSchema,
    CarDeletedSchema,
    CarPatchSchema,
)
from api.response import ValidationInfoSchema
from core.db.models import CarModel
from repository.car_repository.repository import CarRepository
from services.base_service import MainServices
from services.car_services.converter.car_converter import CarConverter
from services.car_services.validator.car_validator import CarValidator


@dataclass
class CarServices(MainServices[CarModel, CarSchema]):
    MODEL = CarModel
    SCHEMA = CarSchema
    repository: CarRepository
    validator: CarValidator
    converter: CarConverter

    async def create(
        self, schema: CarCreateSchema
    ) -> SCHEMA | CarAlreadyExistsSchema | ValidationInfoSchema:

        validation_res = self.validator.is_validate(
            vin=schema.vin,
            gos_nomer=schema.gos_nomer,
        )

        if validation_res.data:
            return validation_res

        obj = await super().get_by_field(key="gos_nomer", value=schema.gos_nomer)
        if obj:
            return CarAlreadyExistsSchema(data=schema.gos_nomer)

        schema.odometer_last = schema.odometer_registered

        model_create = await self.converter.schema_to_model(schema=schema)
        model = await super().create(model=model_create)
        return await self.converter.model_to_schema(model=model)

    async def get(self, id_: UUID) -> SCHEMA | None:
        return await self.converter.model_to_schema(
            await super().get(id_=id_),
        )

    async def delete(self, id_: UUID) -> CarDeletedSchema | None:
        obj = await super().delete(id_)
        if obj:
            return CarDeletedSchema(
                data=await self.converter.model_to_schema(obj), msg="Object deleted"
            )
        return obj

    async def get_by_field(self, key: str, value: str) -> SCHEMA | None:
        obj = await super().get_by_field(key, value)
        if obj:
            return await self.converter.model_to_schema(obj)
        return obj

    async def partial_update(self, data: CarPatchSchema) -> SCHEMA | None:
        model = await super().get(data.id)
        if model:
            upd_model = await super().patch(id_=data.id, data=data.data)
            return await self.converter.model_to_schema(upd_model)
        return model
