from dataclasses import dataclass
from uuid import UUID

from api.customers.schemas.customer import (
    CustomerSchema,
    CustomerCreateSchema,
    CustomerDeleteSchema,
    CustomerPatchSchema,
    CustomerValidateErrorPhoneSchema,
    CustomerAlreadyExistsSchema,
    CustomerCarsSchema,
)
from core.db.models.customers import CustomerModel
from repository.customers_repository.repository import CustomerRepository
from services.base_service import MainServices
from services.customer_services.converter import CustomerConverter
from services.customer_services.validator.validator import CustomerValidator


@dataclass
class CustomerServices(MainServices[CustomerModel, CustomerSchema]):
    MODEL = CustomerModel
    SCHEMA = CustomerSchema
    repository: CustomerRepository
    validator: CustomerValidator
    converter: CustomerConverter

    async def create(
        self, schema: CustomerCreateSchema
    ) -> SCHEMA | CustomerValidateErrorPhoneSchema | CustomerAlreadyExistsSchema:
        if not await self.validator.validate_phone(schema.phone):
            return CustomerValidateErrorPhoneSchema(
                data=schema.phone, msg="Incorrect phone number"
            )

        if await self.get_by_field("phone", schema.phone):
            return CustomerAlreadyExistsSchema(data=schema.phone, msg="Already exists")

        obj = await super().create(await self.converter.schema_to_model(schema))
        return await self.converter.model_to_schema(obj)

    async def get(self, id_: UUID) -> SCHEMA | None:
        obj = await super().get(id_=id_)
        if obj is not None:
            return await self.converter.model_to_schema(obj)
        return obj

    async def delete(self, id_: UUID) -> CustomerDeleteSchema | None:
        obj = await super().delete(id_)
        if obj:
            return CustomerDeleteSchema(
                data=await self.converter.model_to_schema(obj), msg="Object deleted"
            )
        return obj

    async def get_by_field(self, key: str, value: str) -> SCHEMA | None:
        obj = await super().get_by_field(key, value)
        if obj:
            return await self.converter.model_to_schema(obj)
        return obj

    async def partial_update(self, data: CustomerPatchSchema) -> SCHEMA | None:
        model = await super().get(data.id)
        if model:
            upd_model = await super().patch(id_=data.id, data=data.data)
            return await self.converter.model_to_schema(upd_model)
        return model
    
    async def get_cars(self, id_: UUID) -> CustomerCarsSchema | None:
        obj = await super().get(id_ = id_)
        if obj is not None:
            cars = await self.repository.get_cars(id_)
            customer_cars = CustomerCarsSchema()
            for car in cars:
                customer_cars.cars.append(
                    await self.converter.car_model_to_customer_schema(model = car)
                )
            return customer_cars
        return obj
