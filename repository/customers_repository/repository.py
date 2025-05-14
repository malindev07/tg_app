from dataclasses import dataclass
from typing import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.db.helper import db_helper
from core.db.models import CustomerModel
from repository.base_repository import RepositoryORM


@dataclass
class CustomerRepository(RepositoryORM):
    MODEL = CustomerModel
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
    
    async def get_cars(self, id_: UUID) -> Sequence["CarModel"]:
        async with self.session_factory() as session:
            query = (
                select(CustomerModel)
                .options(selectinload(CustomerModel.cars))
                .where(CustomerModel.id == id_)
            )
            res = await session.execute(query)
            customer = res.scalar_one_or_none()
            cars = customer.cars
            return cars
