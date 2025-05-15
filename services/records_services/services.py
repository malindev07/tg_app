from dataclasses import dataclass

from api.records.schema.records import RecordCreateSchema, RecordSchema
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
    
    # async def get(self, id_: UUID) -> SCHEMA | None:
    #     obj = await super().get(id_=id_)
    #     if obj is not None:
    #         return await self.converter.model_to_schema(obj)
    #     return obj
    #
    # async def delete(self, id_: UUID) -> CustomerDeleteSchema | None:
    #     obj = await super().delete(id_)
    #     if obj:
    #         return CustomerDeleteSchema(
    #             data=await self.converter.model_to_schema(obj), msg="Object deleted"
    #         )
    #     return obj
    #
    # async def get_by_field(self, key: str, value: str) -> SCHEMA | None:
    #     obj = await super().get_by_field(key, value)
    #     if obj:
    #         return await self.converter.model_to_schema(obj)
    #     return obj
    #
    # async def partial_update(self, data: CustomerPatchSchema) -> SCHEMA | None:
    #     model = await super().get(data.id)
    #     if model:
    #         upd_model = await super().patch(id_=data.id, data=data.data)
    #         return await self.converter.model_to_schema(upd_model)
    #     return model
