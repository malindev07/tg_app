from dataclasses import dataclass
from typing import Sequence

from api.records.schema.record_schema import (
    RecordSchema,
    RecordCreateSchema,
    RecordWithAssociationSchema,
    RecordWithStaffSchema,
)
from core.db.models.records import RecordModel


@dataclass
class RecordConverter:
    async def schema_to_model(
        self, schema: RecordSchema | RecordCreateSchema
    ) -> RecordModel:
        return RecordModel(
            client_id=schema.client_id,
            car_id=schema.car_id,
            reason=schema.reason,
            comment=schema.comment,
            record_date=schema.record_date,
            start_time=schema.start_time,
            end_time=schema.end_time,
        )

    async def model_to_schema(self, model: RecordModel) -> RecordSchema:
        return RecordSchema(
            client_id=model.client_id,
            car_id=model.car_id,
            reason=model.reason,
            comment=model.comment,
            record_date=model.record_date,
            start_time=model.start_time,
            end_time=model.end_time,
            id=model.id,
            status=model.status,
        )

    async def model_with_staff_to_schema(
            self, model: RecordModel
    ) -> RecordWithStaffSchema:
        staff_ids = [
            association.staff_id for association in model.workstation_staff_associations
        ]

        return RecordWithStaffSchema(
            client_id=model.client_id,
            car_id=model.car_id,
            reason=model.reason,
            comment=model.comment,
            record_date=model.record_date,
            start_time=model.start_time,
            end_time=model.end_time,
            id=model.id,
            status=model.status,
            staff_id=staff_ids,
        )

    async def model_with_association_to_schema(
        self, models: Sequence[RecordModel]
    ) -> Sequence[RecordWithAssociationSchema]:
        records = list()

        for model in models:
            staff_ids = [
                association.staff_id
                for association in model.workstation_staff_associations
            ]
            workstation_id = model.workstation_staff_associations[
                0
            ].workstation_id  # TODO ПОДУМАТЬ КАК ИСПРАВИТЬ
            records.append(
                RecordWithAssociationSchema(
                    client_id=model.client_id,
                    workstation_id=workstation_id,
                    car_id=model.car_id,
                    reason=model.reason,
                    comment=model.comment,
                    record_date=model.record_date,
                    start_time=model.start_time,
                    end_time=model.end_time,
                    id=model.id,
                    status=model.status,
                    staff_id=staff_ids,
                )
            )
        return records
