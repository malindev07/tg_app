from dataclasses import dataclass
from uuid import UUID

from core.db.helper import db_helper
from core.db.models import StaffModel
from repository.base_repository import RepositoryORM


@dataclass
class StaffRepository(RepositoryORM):
    MODEL = StaffModel
    session_factory = db_helper.session_factory

    async def create(self, model: MODEL) -> MODEL:
        return await super().create(model=model)

    async def get(self, id_: UUID) -> MODEL:
        return await super().get(id_=id_)

    async def get_by_field(self, key: str, value: str) -> MODEL | None:
        return await super().get_by_field(key=key, value=value)

    async def delete(self, model: MODEL) -> None:
        return await super().delete(model)

    async def update(self) -> MODEL: ...
