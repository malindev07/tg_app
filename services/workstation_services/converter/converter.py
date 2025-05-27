from dataclasses import dataclass

from api.workstations.schema.workstation_schema import (
    WorkstationSchema,
    WorkstationCreateSchema,
)
from core.db.models import WorkstationModel


@dataclass
class WorkstationConverter:
    async def schema_to_model(
        self, schema: WorkstationSchema | WorkstationCreateSchema
    ) -> WorkstationModel:
        return WorkstationModel(
            title=schema.title,
            description=schema.description,
            start_time=schema.start_time,
            end_time=schema.end_time,
        )

    async def model_to_schema(self, model: WorkstationModel) -> WorkstationSchema:
        return WorkstationSchema(
            id=model.id,
            title=model.title,
            status=model.status,
            description=model.description,
            start_time=model.start_time,
            end_time=model.end_time,
        )
