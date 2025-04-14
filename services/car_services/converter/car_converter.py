from dataclasses import dataclass

from api.cars.schemas.schema import CarSchema, CarCreateSchema
from core.db.models import CarModel


@dataclass
class CarConverter:
    async def schema_to_model(self, schema: CarSchema | CarCreateSchema) -> CarModel:
        return CarModel(
            gos_nomer=schema.gos_nomer,
            brand=schema.gos_nomer,
            model=schema.model,
            vin=schema.vin,
        )

    async def model_to_schema(self, model: CarModel) -> CarSchema:
        return CarSchema(
            id=model.id,
            gos_nomer=model.gos_nomer,
            brand=model.gos_nomer,
            model=model.model,
            vin=model.vin,
        )
