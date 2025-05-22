from dataclasses import dataclass

from api.staff.schema.staff_schema import StaffSchema, StaffCreateSchema
from core.db.models import StaffModel


@dataclass
class StaffConverter:
    async def schema_to_model(
        self, schema: StaffSchema | StaffCreateSchema
    ) -> StaffModel:
        return StaffModel(
            position=schema.position,
            first_name=schema.first_name,
            last_name=schema.last_name,
            middle_name=schema.middle_name,
            phone=schema.phone,
            salary_rate=schema.salary_rate,
            comment=schema.comment,
        )

    async def model_to_schema(self, model: StaffModel) -> StaffSchema:
        return StaffSchema(
            id=model.id,
            position=model.position,
            first_name=model.first_name,
            last_name=model.last_name,
            middle_name=model.middle_name,
            phone=model.phone,
            status=model.status,
            salary_rate=model.salary_rate,
            comment=model.comment,
        )
