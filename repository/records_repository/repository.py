from dataclasses import dataclass
from datetime import date
from typing import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.db.helper import db_helper
from core.db.models import WorkstationStaffRecordAssociationModel
from core.db.models.records import RecordModel
from repository.base_repository import RepositoryORM


@dataclass
class RecordsRepository(RepositoryORM):
    MODEL = RecordModel
    RECORD_STAFF_WORKSTATION_ASSOCIATION_MODEL = WorkstationStaffRecordAssociationModel
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

    async def create_with_association(
        self, model: MODEL, staff_id: UUID, workstation_id: UUID
    ):
        async with self.session_factory() as session:
            try:
                session.add(model)
                await session.flush()

                session.add(
                    self.RECORD_STAFF_WORKSTATION_ASSOCIATION_MODEL(
                        record_id=model.id,
                        staff_id=staff_id,
                        workstation_id=workstation_id,
                    )
                )
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

            return model

    async def get_with_staff(self, record_id: UUID):
        async with self.session_factory() as session:
            result = await session.execute(
                select(RecordModel)
                .options(selectinload(RecordModel.workstation_staff_associations))
                .where(RecordModel.id == record_id)
            )
            record = result.scalars().first()
            return record

    async def get_by_date_and_workstation(self, rec_date: date, workstation_id: UUID):
        # TODO исправить!!! Неправильно отдает данные
        async with self.session_factory() as session:
            query = (
                select(RecordModel)
                .join(
                    WorkstationStaffRecordAssociationModel,
                    RecordModel.id == WorkstationStaffRecordAssociationModel.record_id,
                )
                .where(
                    RecordModel.record_date == rec_date,
                    WorkstationStaffRecordAssociationModel.workstation_id
                    == workstation_id,
                )
                .options(selectinload(RecordModel.workstation_staff_associations))
            )
            res = await session.execute(query)
            records = res.scalars().all()
            return records

    async def get_by_date_and_staff(self, rec_date: date, staff_id: UUID):
        async with self.session_factory() as session:
            query = (
                select(RecordModel)
                .join(
                    WorkstationStaffRecordAssociationModel,
                    RecordModel.id == WorkstationStaffRecordAssociationModel.record_id,
                )
                .where(
                    RecordModel.record_date == rec_date,
                    WorkstationStaffRecordAssociationModel.staff_id == staff_id,
                )
                .options(selectinload(RecordModel.workstation_staff_associations))
            )
            res = await session.execute(query)
            records = res.scalars().all()
            return records
