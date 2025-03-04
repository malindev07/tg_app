from dataclasses import dataclass

from sqlalchemy.exc import DataError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from repository.db.models.car_model import CarORM


@dataclass
class CarRepositoryORM:
    session: async_sessionmaker[AsyncSession]

    async def create_car(self, car: CarORM) -> bool:
        async with self.session() as session:
            try:
                session.add(car)
            except:
                await session.rollback()
                raise
            else:
                await session.commit()
                return True

    async def find_car_by_id(self, car_id: str) -> CarORM | None:
        async with self.session() as session:
            try:
                find_car = await session.get(CarORM, car_id)
            except:
                await session.rollback()
                raise
            else:
                return find_car
