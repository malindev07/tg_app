from uuid import UUID
from dataclasses import dataclass
from core.db.models import CarModel
from core.db.helper import db_helper
from repository.base_repository import RepositoryORM


@dataclass
class CarRepository(RepositoryORM):
    MODEL = CarModel
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
