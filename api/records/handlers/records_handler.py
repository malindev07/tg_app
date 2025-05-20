from datetime import date
from typing import Sequence
from uuid import UUID

from fastapi import APIRouter, Request

from api.records.schema.records import (
    RecordCreateSchema,
    RecordPatchSchema,
    RecordSchema,
    RecordDeleteSchema,
)
from api.response import KeyValueNotFoundSchema, IDNotFoundSchema

record_router = APIRouter(prefix="/record", tags=["Record"])


@record_router.post("/")
async def create(request: Request, data: RecordCreateSchema) -> RecordSchema:
    return await request.state.records_services.create(schema=data)


@record_router.get("/")
async def get(request: Request, id_: UUID) -> RecordSchema | IDNotFoundSchema:
    return await request.state.records_services.get(id_=id_)


@record_router.delete("/")
async def delete(request: Request, id_: UUID) -> RecordDeleteSchema | IDNotFoundSchema:
    return await request.state.records_services.delete(id_=id_)


@record_router.get("/by-{key}/{value}")
async def get_by_field(
    request: Request, key: str, value: str
) -> RecordSchema | KeyValueNotFoundSchema:
    return await request.state.records_services.get_by_field(key, value)


@record_router.patch("/")
async def patch(
    request: Request, data: RecordPatchSchema
) -> RecordSchema | IDNotFoundSchema:
    return await request.state.records_services.partial_update(data=data)


@record_router.get("/{record_date}/")
async def get_by_date(
    request: Request, record_date: date
) -> Sequence[RecordSchema] | None:
    return await request.state.records_services.get_by_date(record_date=record_date)
