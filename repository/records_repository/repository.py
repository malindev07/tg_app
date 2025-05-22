from dataclasses import dataclass
from datetime import date
from typing import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.db.helper import db_helper
from core.db.models.record_staff_association import RecordStaffAssociationModel
from core.db.models.records import RecordModel
from repository.base_repository import RepositoryORM


@dataclass
class RecordsRepository(RepositoryORM):
    MODEL = RecordModel
    RECORD_STAFF_ASSOCIATION_MODEL = RecordStaffAssociationModel
    session_factory = db_helper.session_factory

    async def create(
        self,
        model: MODEL,
    ) -> MODEL:
        record = await super().create(model=model)
        return record

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

    async def create_with_association(self, model: MODEL, staff_id: list[UUID]):
        async with self.session_factory() as session:
            record = await super().create(model)
            session.add(record)
            await session.flush()
            for id_ in staff_id:
                session.add(
                    self.RECORD_STAFF_ASSOCIATION_MODEL(
                        record_id=record.id, staff_id=id_
                    )
                )
            await session.commit()
            return record

    async def get_with_staff(self, record_id: UUID):
        async with self.session_factory() as session:
            result = await session.execute(
                select(RecordModel)
                .options(selectinload(RecordModel.staff_associations))
                .where(RecordModel.id == record_id)
            )
            record = result.scalars().first()
            return record
