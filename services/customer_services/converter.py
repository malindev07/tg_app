from dataclasses import dataclass

from api.customers.schemas.customer import CustomerSchema, CreateCustomerSchema
from core.db.models.customers import CustomerModel


@dataclass
class CustomerConverter:
    async def schema_to_model(
        self, schema: CustomerSchema | CreateCustomerSchema
    ) -> CustomerModel:
        return CustomerModel(
            first_name=schema.first_name,
            last_name=schema.last_name,
            middle_name=schema.middle_name,
            phone=schema.phone,
        )

    # async def model_to_schema(self, model: CarModel) -> CarSchema:
    #     return CarSchema(
    #         id=model.id,
    #         gos_nomer=model.gos_nomer,
    #         brand=model.gos_nomer,
    #         model=model.model,
    #         vin=model.vin,
    #     )
