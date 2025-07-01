from dataclasses import dataclass
from uuid import UUID

from api.response import IDNotFoundSchema, KeyValueNotFoundSchema
from api.workstations.schema.workstation_schema import (
    WorkstationDeleteSchema,
    WorkstationCreateSchema,
    WorkstationSchema,
    WorkstationPatchSchema,
)
from core.db.models import WorkstationModel
from repository.workstation_repository.repository import WorkstationRepository
from services.base_service import MainServices
from services.workstation_services.converter.converter import WorkstationConverter


@dataclass
class WorkstationServices(MainServices[WorkstationModel, WorkstationSchema]):
    MODEL = WorkstationModel
    SCHEMA = WorkstationSchema
    repository: WorkstationRepository
    converter: WorkstationConverter

    async def create(self, schema: WorkstationCreateSchema) -> SCHEMA:
        obj = await super().create(await self.converter.schema_to_model(schema))

        return await self.converter.model_to_schema(obj)

    async def get(self, id_: UUID) -> SCHEMA | IDNotFoundSchema:
        obj = await super().get(id_=id_)
        if obj is not None:
            return await self.converter.model_to_schema(obj)
        return IDNotFoundSchema(id_=id_)

    async def delete(self, id_: UUID) -> WorkstationDeleteSchema | IDNotFoundSchema:
        obj = await super().delete(id_)
        if obj:
            return WorkstationDeleteSchema(
                data=await self.converter.model_to_schema(obj), msg="Object deleted"
            )
        return IDNotFoundSchema(id_=id_)

    async def get_by_field(
        self, key: str, value: str
    ) -> SCHEMA | KeyValueNotFoundSchema:
        obj = await super().get_by_field(key, value)
        if obj:
            return await self.converter.model_to_schema(obj)
        return KeyValueNotFoundSchema(data=dict[key, value])

    async def partial_update(
        self, data: WorkstationPatchSchema
    ) -> SCHEMA | IDNotFoundSchema:
        model = await super().get(data.id)
        if model:
            upd_model = await super().patch(id_=data.id, data=data.data)
            return await self.converter.model_to_schema(upd_model)
        return IDNotFoundSchema(id_=data.id)
