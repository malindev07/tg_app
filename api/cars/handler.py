from uuid import UUID

import httpx
from fastapi import APIRouter, Request

from api.cars.schema import (
    CarCreateSchema,
    CarDeletedSchema,
    CarSchema,
    CarAlreadyExistsSchema,
    CarPatchSchema,
)
from api.response import ValidationInfoSchema, IDNotFoundSchema

car_router = APIRouter(prefix="/car", tags=["Car"])


async def call_customer_get_endpoint(id_: UUID):
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get(f"/customer/", params={"id_": str(id_)})
        return response.json()


@car_router.post("/")
async def create(
    request: Request, schema: CarCreateSchema
) -> CarSchema | CarAlreadyExistsSchema | ValidationInfoSchema | IDNotFoundSchema:
    if await call_customer_get_endpoint(schema.owner_id) is None:
        return IDNotFoundSchema(id_=schema.owner_id, msg="Owner not found")
    return await request.state.car_services.create(schema=schema)


@car_router.get("/")
# Поиск всех сущностей
async def get(request: Request, id_: UUID) -> CarSchema:
    return await request.state.car_services.get(id_=id_)


@car_router.get("/{id_}")
# Поиск сущности по id
async def get(request: Request, id_: UUID) -> CarSchema:
    return await request.state.car_services.get(id_=id_)


@car_router.get("/by-{key}/{value}")
async def get_by_field(request: Request, key: str, value: str) -> CarSchema:
    return await request.state.car_services.get_by_field(key, value)


@car_router.delete("/{id_}")
async def delete(request: Request, id_: UUID) -> CarDeletedSchema | None:
    return await request.state.car_services.delete(id_)


@car_router.patch("/")
async def patch(request: Request, data: CarPatchSchema) -> CarSchema | None:
    return await request.state.car_services.partial_update(data=data)
