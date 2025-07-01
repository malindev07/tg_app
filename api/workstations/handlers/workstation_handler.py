from uuid import UUID

from fastapi import APIRouter, Request

from api.response import KeyValueNotFoundSchema, IDNotFoundSchema
from api.url_settings import UrlPrefix
from api.workstations.schema.workstation_schema import (
    WorkstationCreateSchema,
    WorkstationSchema,
    WorkstationDeleteSchema,
    WorkstationPatchSchema,
)

workstation_router = APIRouter(prefix=UrlPrefix.workstation, tags=["workstation"])


@workstation_router.post("/")
async def create(request: Request, data: WorkstationCreateSchema) -> WorkstationSchema:
    return await request.state.workstation_services.create(schema=data)


@workstation_router.get("/")
async def get(request: Request, id_: UUID) -> WorkstationSchema | IDNotFoundSchema:
    return await request.state.workstation_services.get(id_=id_)


@workstation_router.delete("/")
async def delete(
    request: Request, id_: UUID
) -> WorkstationDeleteSchema | IDNotFoundSchema:
    return await request.state.workstation_services.delete(id_=id_)


@workstation_router.get("/by-{key}/{value}")
async def get_by_field(
    request: Request, key: str, value: str
) -> WorkstationSchema | KeyValueNotFoundSchema:
    return await request.state.workstation_services.get_by_field(key, value)


@workstation_router.patch("/")
async def patch(
    request: Request, data: WorkstationPatchSchema
) -> WorkstationSchema | IDNotFoundSchema:
    return await request.state.workstation_services.partial_update(data=data)
