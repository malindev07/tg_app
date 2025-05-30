from datetime import date
from typing import Sequence
from uuid import UUID

from fastapi import APIRouter, Request
from starlette import status

from api.records.schema.record_schema import (
    RecordCreateSchema,
    RecordPatchSchema,
    RecordSchema,
    RecordDeleteSchema,
    RecordWithAssociationSchema,
    RecordWithStaffSchema,
)
from api.response import KeyValueNotFoundSchema, IDNotFoundSchema

record_router = APIRouter(prefix="/record", tags=["Record"])


@record_router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=RecordSchema
)
async def create(request: Request, data: RecordCreateSchema) -> RecordSchema:

    return await request.state.records_services.create(schema=data)


@record_router.get("/{id_}", response_model=RecordSchema | IDNotFoundSchema)
async def get(request: Request, id_: UUID) -> RecordSchema | IDNotFoundSchema:
    return await request.state.records_services.get(id_=id_)


@record_router.delete("/{id_}", response_model=RecordDeleteSchema | IDNotFoundSchema)
async def delete(request: Request, id_: UUID) -> RecordDeleteSchema | IDNotFoundSchema:
    # todo сделать проверку на возможность удаления, если невозможно удалить, менять статус записи
    return await request.state.records_services.delete(id_=id_)


@record_router.get("/", response_model=RecordSchema | KeyValueNotFoundSchema)
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


@record_router.get("/{record_id}/staff")
async def get_with_staff(request: Request, record_id: UUID) -> RecordWithStaffSchema:
    return await request.state.records_services.get_with_staff(record_id=record_id)


@record_router.get("/{rec_date}/{workstation_id}/")
async def get_by_date_and_workstation(
    request: Request,
    rec_date: date,
    workstation_id: UUID,
    # start_time: str = Query(..., description="Start time in HH:MM format"),
    # end_time: str = Query(..., description="End time in HH:MM format"),
) -> Sequence[RecordWithAssociationSchema]:
    return await request.state.records_services.get_by_date_and_workstation(
        rec_date, workstation_id
    )
