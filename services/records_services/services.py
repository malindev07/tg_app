from dataclasses import dataclass
from datetime import date
from typing import Sequence
from uuid import UUID

from api.records.schema.records import (
    RecordCreateSchema,
    RecordSchema,
    RecordDeleteSchema,
    RecordPatchSchema,
)
from api.response import IDNotFoundSchema, KeyValueNotFoundSchema
from core.db.models.records import RecordModel
from repository.records_repository.repository import RecordsRepository
from services.base_service import MainServices
from services.records_services.converter.converter import RecordConverter


@dataclass
class RecordsServices(MainServices[RecordModel, RecordSchema]):
    MODEL = RecordModel
    SCHEMA = RecordSchema
    repository: RecordsRepository
    # validator: CustomerValidator
    converter: RecordConverter

    async def create(self, schema: RecordCreateSchema):
        obj = await super().create(await self.converter.schema_to_model(schema))
        
        return obj
    
    async def get(self, id_: UUID) -> SCHEMA | IDNotFoundSchema:
        obj = await super().get(id_ = id_)
        if obj is not None:
            return await self.converter.model_to_schema(obj)
        return IDNotFoundSchema(id_ = id_)
    
    async def delete(self, id_: UUID) -> RecordDeleteSchema | IDNotFoundSchema:
        obj = await super().delete(id_)
        if obj:
            return RecordDeleteSchema(
                data = await self.converter.model_to_schema(obj), msg = "Object deleted"
            )
        return IDNotFoundSchema(id_ = id_)
    
    async def get_by_field(
            self, key: str, value: str
    ) -> SCHEMA | KeyValueNotFoundSchema:
        obj = await super().get_by_field(key, value)
        if obj:
            return await self.converter.model_to_schema(obj)
        return KeyValueNotFoundSchema(data = dict[key, value])
    
    async def partial_update(
            self, data: RecordPatchSchema
    ) -> SCHEMA | IDNotFoundSchema:
        model = await super().get(data.id)
        if model:
            upd_model = await super().patch(id_ = data.id, data = data.data)
            return await self.converter.model_to_schema(upd_model)
        return IDNotFoundSchema(id_ = data.id)
    
    async def get_by_date(self, record_date: date) -> Sequence[RecordSchema] | None:
        objs = await self.repository.get_by_date(record_date)
        if objs:
            return [await self.converter.model_to_schema(obj) for obj in objs]
        
        return None
