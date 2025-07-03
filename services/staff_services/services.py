from dataclasses import dataclass
from uuid import UUID

from api.response import (
    IDNotFoundSchema,
    KeyValueNotFoundSchema,
    ValidationInfoSchema,
    AlreadyExistSchema,
)
from api.staff.schema.staff_schema import (
    StaffSchema,
    StaffDeleteSchema,
    StaffPatchSchema,
    StaffCreateSchema,
)
from core.db.models import StaffModel
from repository.staff_repository.repository import StaffRepository
from services.base_service import MainServices
from services.staff_services.converter.converter import StaffConverter
from services.staff_services.validator.validator import StaffValidator


@dataclass
class StaffServices(MainServices[StaffModel, StaffSchema]):
    MODEL = StaffModel
    SCHEMA = StaffSchema
    repository: StaffRepository
    validator: StaffValidator
    converter: StaffConverter
    
    async def create(
            self, schema: StaffCreateSchema
    ) -> SCHEMA | ValidationInfoSchema | AlreadyExistSchema:
        validation_info = await self.validator.is_validate(schema.phone)
        
        if validation_info.data:
            return validation_info
        
        if await self.repository.get_by_field(key = "phone", value = schema.phone):
            return AlreadyExistSchema(data = schema.phone)
        
        obj = await self.repository.create(await self.converter.schema_to_model(schema))
        return await self.converter.model_to_schema(obj)

    async def get(self, id_: UUID) -> SCHEMA | IDNotFoundSchema:
        obj = await super().get(id_=id_)
        if obj is not None:
            return await self.converter.model_to_schema(obj)
        return IDNotFoundSchema(id_=id_)

    async def delete(self, id_: UUID) -> StaffDeleteSchema | IDNotFoundSchema:
        obj = await super().delete(id_)
        if obj:
            return StaffDeleteSchema(
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

    async def partial_update(self, data: StaffPatchSchema) -> SCHEMA | IDNotFoundSchema:
        model = await super().get(data.id)
        if model:
            upd_model = await super().patch(id_=data.id, data=data.data)
            return await self.converter.model_to_schema(upd_model)
        return IDNotFoundSchema(id_=data.id)
