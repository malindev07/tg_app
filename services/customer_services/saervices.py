from dataclasses import dataclass

from api.customers.schemas.customer import CustomerSchema, CreateCustomerSchema
from core.db.models.customers import CustomerModel
from services.base_service import MainServices
from services.customer_services.converter import CustomerConverter


@dataclass
class CustomerServices(MainServices[CustomerModel, CustomerSchema]):
    MODEL = CustomerModel
    SCHEMA = CustomerSchema
    # repository: CarRepository
    # validator: CarValidator
    converter: CustomerConverter

    async def create(self, customer: CreateCustomerSchema):

        obj = await super().create(await self.converter.schema_to_model(customer))
        return obj
