from dataclasses import dataclass

from api.cars.schema import CarSchema, CarCreateSchema
from core.db.models import CarModel


@dataclass
class CarConverter:
    async def schema_to_model(self, schema: CarSchema | CarCreateSchema) -> CarModel:
        return CarModel(
            gos_nomer=schema.gos_nomer,
            brand=schema.gos_nomer,
            model=schema.model,
            vin=schema.vin,
            odometer_registered=schema.odometer_registered,
            odometer_last=schema.odometer_last,
            owner_id=schema.owner_id,
        )

    async def model_to_schema(self, model: CarModel) -> CarSchema:
        return CarSchema(
            id=model.id,
            gos_nomer=model.gos_nomer,
            brand=model.gos_nomer,
            model=model.model,
            vin=model.vin,
            odometer_registered=model.odometer_registered,
            odometer_last=model.odometer_last,
        )
