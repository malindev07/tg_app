from dataclasses import dataclass

from api.records.schema.record_schema import (
    RecordSchema,
    RecordCreateSchema,
    RecordWithAssociationSchema,
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

    async def model_with_association_to_schema(
        self, model: RecordModel
    ) -> RecordWithAssociationSchema:
        staff_ids = [association.staff_id for association in model.staff_associations]

        return RecordWithAssociationSchema(
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
