from uuid import UUID

from fastapi import APIRouter, Request

from api.cars.schemas.car_schema import (
    CarCreateSchema,
    CarDeletedSchema,
    CarSchema,
    CarAlreadyExistsSchema,
    CarValidationInfoSchema,
    CarPatchSchema,
)

car_router = APIRouter(prefix="/car", tags=["Car"])


@car_router.post("/")
async def create(
    request: Request, schema: CarCreateSchema
) -> CarSchema | CarAlreadyExistsSchema | CarValidationInfoSchema:
    return await request.state.car_services.create(schema=schema)


@car_router.get("/{id_}")
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
