from dataclasses import dataclass

from api.customers.schemas.customer import CustomerSchema, CustomerCreateSchema
from core.db.models.customers import CustomerModel


@dataclass
class CustomerConverter:
    async def schema_to_model(
            self, schema: CustomerSchema | CustomerCreateSchema
    ) -> CustomerModel:
        return CustomerModel(
            first_name=schema.first_name,
            last_name=schema.last_name,
            middle_name=schema.middle_name,
            phone=schema.phone,
        )
    
    async def model_to_schema(self, model: CustomerModel) -> CustomerSchema:
        return CustomerSchema(
            id = model.id,
            first_name = model.first_name,
            last_name = model.last_name,
            middle_name = model.middle_name,
            phone = model.phone,
            is_verify = model.is_verify,
            tg_id = model.tg_id,
            discount = model.discount,
        )
