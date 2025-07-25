from dataclasses import dataclass
from datetime import date, datetime
from typing import Sequence
from uuid import UUID

import httpx

from api.records.schema import (
    RecordCreateSchema,
    RecordSchema,
    RecordDeleteSchema,
    RecordPatchSchema,
    RecordWithAssociationSchema,
    RecordWithStaffSchema,
)
from api.response import IDNotFoundSchema, KeyValueNotFoundSchema, ValidationInfoSchema
from api.workstations.schema import WorkstationSchema
from core.db.models.records import RecordModel
from repository.records_repository.repository import RecordsRepository
from services.base_service import MainServices
from services.records_services.converter import RecordConverter
from services.records_services.validator import RecordValidator

MIN_RECORD_TIME = 30


async def call_workstation_get_endpoint(id_: UUID):
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get(f"/workstation/", params={"id_": str(id_)})
        return response.json()


@dataclass
class RecordsServices(MainServices[RecordModel, RecordSchema]):
    MODEL = RecordModel
    SCHEMA = RecordSchema
    repository: RecordsRepository
    validator: RecordValidator
    converter: RecordConverter

    async def create(self, schema: RecordCreateSchema) -> SCHEMA | ValidationInfoSchema:

        ws = WorkstationSchema(
            **await call_workstation_get_endpoint(id_=schema.workstation_id)
        )

        start_dt_new = datetime.combine(datetime.today(), schema.start_time)
        end_dt_new = datetime.combine(datetime.today(), schema.end_time)

        validation_info = await self.validator.is_validate(
            start_time=start_dt_new,
            end_time=end_dt_new,
            records=await self.get_by_date_and_staff(
                schema.record_date, schema.staff_id
            ),
            workstation=ws,
        )

        if validation_info.data:
            return validation_info

        obj = await self.repository.create_with_association(
            model=await self.converter.schema_to_model(schema),
            staff_id=schema.staff_id,
            workstation_id=schema.workstation_id,
        )

        return await self.converter.model_to_schema(obj)

    async def get(self, id_: UUID) -> SCHEMA | IDNotFoundSchema:
        obj = await super().get(id_=id_)
        if obj is not None:
            return await self.converter.model_to_schema(obj)
        return IDNotFoundSchema(id_=id_)

    async def delete(self, id_: UUID) -> RecordDeleteSchema | IDNotFoundSchema:
        obj = await super().delete(id_)
        if obj:
            return RecordDeleteSchema(
                data=await self.converter.model_to_schema(obj), msg="Object deleted"
            )
        return IDNotFoundSchema(id_=id_)

    async def get_by_field(
        self, key: str, value: str
    ) -> SCHEMA | KeyValueNotFoundSchema:
        obj = await super().get_by_field(key, value)
        if obj:
            return await self.converter.model_to_schema(obj)
        return KeyValueNotFoundSchema(data=dict[key, value])

    async def partial_update(
        self, data: RecordPatchSchema
    ) -> SCHEMA | IDNotFoundSchema:
        model = await super().get(data.id)
        if model:
            upd_model = await super().patch(id_=data.id, data=data.data)
            return await self.converter.model_to_schema(upd_model)
        return IDNotFoundSchema(id_=data.id)

    async def get_by_date(self, record_date: date) -> Sequence[RecordSchema] | None:
        objs = await self.repository.get_by_date(record_date)
        if objs:
            return [await self.converter.model_to_schema(obj) for obj in objs]

        return None

    async def get_with_staff(self, record_id: UUID) -> RecordWithStaffSchema:
        return await self.converter.model_with_staff_to_schema(
            await self.repository.get_with_staff(record_id)
        )

    async def get_by_date_and_workstation(
        self, rec_date: date, workstation_id: UUID
    ) -> Sequence[RecordWithAssociationSchema]:
        records = await self.repository.get_by_date_and_workstation(
            rec_date, workstation_id
        )
        return await self.converter.model_with_association_to_schema(
            records
        )  # TODO Уточнить как возвращать из одной сущности другую(в записи указывать фио мастера)

    async def get_by_date_and_staff(
        self, rec_date: date, staff_id: UUID
    ) -> Sequence[RecordWithAssociationSchema]:
        records = await self.repository.get_by_date_and_staff(rec_date, staff_id)

        return await self.converter.model_with_association_to_schema(records)
