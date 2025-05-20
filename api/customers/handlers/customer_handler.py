from uuid import UUID

from fastapi import APIRouter, Request

from api.customers.schemas.customer import (
    CustomerCreateSchema,
    CustomerSchema,
    CustomerDeleteSchema,
    CustomerPatchSchema,
    CustomerValidateErrorPhoneSchema,
    CustomerAlreadyExistsSchema,
    CustomerCarsSchema,
)

customer_router = APIRouter(prefix="/customer", tags=["Customer"])


@customer_router.post("/")
async def create(
    request: Request, data: CustomerCreateSchema
) -> CustomerSchema | CustomerValidateErrorPhoneSchema | CustomerAlreadyExistsSchema:
    return await request.state.customer_services.create(schema=data)


@customer_router.get("/")
async def get(request: Request, id_: UUID) -> CustomerSchema | None:
    return await request.state.customer_services.get(id_=id_)


@customer_router.delete("/")
async def delete(request: Request, id_: UUID) -> CustomerDeleteSchema | None:
    return await request.state.customer_services.delete(id_=id_)


@customer_router.get("/by-{key}/{value}")
async def get_by_field(request: Request, key: str, value: str) -> CustomerSchema | None:
    return await request.state.customer_services.get_by_field(key, value)


@customer_router.patch("/")
async def patch(request: Request, data: CustomerPatchSchema) -> CustomerSchema | None:
    return await request.state.customer_services.partial_update(data=data)


@customer_router.get("/{id_}/cars")
async def get_cars(request: Request, id_: UUID) -> CustomerCarsSchema | None:
    return await request.state.customer_services.get_cars(id_)
