from dataclasses import dataclass
from datetime import date
from typing import Sequence
from uuid import UUID

from sqlalchemy import select

from core.db.helper import db_helper
from core.db.models.records import RecordModel
from repository.base_repository import RepositoryORM


@dataclass
class RecordsRepository(RepositoryORM):
    MODEL = RecordModel
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

    async def get_by_date(self, record_date: date) -> Sequence[RecordModel]:
        async with self.session_factory() as session:
            query = select(self.MODEL).where(self.MODEL.record_date == record_date)
            res = await session.execute(query)
            records = res.scalars().all()
            return records
