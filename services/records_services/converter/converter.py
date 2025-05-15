from dataclasses import dataclass

from api.records.schema.records import RecordSchema, RecordCreateSchema
from core.db.models.records import RecordModel


@dataclass
class RecordConverter:
    async def schema_to_model(
            self, schema: RecordSchema | RecordCreateSchema
    ) -> RecordModel:
        return RecordModel(
            client_id = schema.client_id,
            car_id = schema.car_id,
            reason = schema.reason,
            comment = schema.comment,
            record_date = schema.record_date,
            start_time = schema.start_time,
            end_time = schema.end_time,
        )
    
    # async def model_to_schema(self, model: CustomerModel) -> CustomerSchema:
    #     return CustomerSchema(
    #         id=model.id,
    #         first_name=model.first_name,
    #         last_name=model.last_name,
    #         middle_name=model.middle_name,
    #         phone=model.phone,
    #         is_verify=model.is_verify,
    #         tg_id=model.tg_id,
    #         discount=model.discount,
    #     )
