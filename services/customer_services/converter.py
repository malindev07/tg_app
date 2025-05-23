from dataclasses import dataclass

from api.cars.schemas.car_schema import CarSchema
from api.customers.schemas.customer_schema import CustomerSchema, CustomerCreateSchema
from core.db.models import CarModel
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
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            middle_name=model.middle_name,
            phone=model.phone,
            is_verify=model.is_verify,
            tg_id=model.tg_id,
            discount=model.discount,
        )

    async def car_model_to_customer_schema(self, model: CarModel) -> CarSchema:
        return CarSchema(
            id=model.id,
            gos_nomer=model.gos_nomer,
            brand=model.gos_nomer,
            model=model.model,
            vin=model.vin,
            odometer_registered=model.odometer_registered,
            odometer_last=model.odometer_last,
        )
