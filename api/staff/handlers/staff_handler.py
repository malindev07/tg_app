from uuid import UUID

from fastapi import APIRouter, Request

from api.response import (
    KeyValueNotFoundSchema,
    IDNotFoundSchema,
    ValidationInfoSchema,
    AlreadyExistSchema,
)
from api.staff.schema.staff_schema import (
    StaffCreateSchema,
    StaffPatchSchema,
    StaffSchema,
    StaffDeleteSchema,
)
from api.url_settings import UrlPrefix

staff_router = APIRouter(prefix=UrlPrefix.staff, tags=["Staff"])


@staff_router.post("/")
async def create(
        request: Request, data: StaffCreateSchema
) -> StaffSchema | ValidationInfoSchema | AlreadyExistSchema:
    return await request.state.staff_services.create(schema=data)


@staff_router.get("/")
async def get(request: Request, id_: UUID) -> StaffSchema | IDNotFoundSchema:
    return await request.state.staff_services.get(id_=id_)


@staff_router.delete("/")
async def delete(request: Request, id_: UUID) -> StaffDeleteSchema | IDNotFoundSchema:
    return await request.state.staff_services.delete(id_=id_)


@staff_router.get("/by-{key}/{value}")
async def get_by_field(
    request: Request, key: str, value: str
) -> StaffSchema | KeyValueNotFoundSchema:
    return await request.state.staff_services.get_by_field(key, value)


@staff_router.patch("/")
async def patch(
    request: Request, data: StaffPatchSchema
) -> StaffSchema | IDNotFoundSchema:
    return await request.state.staff_services.partial_update(data=data)
