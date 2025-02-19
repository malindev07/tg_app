from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from repository.db.models.car_model import CarORM
from repository.db.settings.helper import db_helper


# from repository.db.settings.helper import db_helper


@dataclass
class DataBaseCarAction:
    db_session: async_sessionmaker[AsyncSession] = db_helper.session_factory()

    # Сохранение авто в бд
    async def save_car_db(self, car: CarORM) -> CarORM | bool:
        try:
            async with self.db_session as session:
                session.add(car)
                await session.commit()
                print(car.car_id, "saved")
                return True

        except IntegrityError:
            print(car.car_id, "not saved")
            return False

    # Поиск авто по гос номеру

    async def search_car_db(self, car_id: str) -> CarORM | None:
        try:
            async with self.db_session as session:

                car = await session.get(CarORM, car_id)
                print(car.car_id, "found")
                return car

        except AttributeError:
            print(car_id, "not found")
            return None

    # Обновление гос номера авто

    async def update_car_id_db(self, car_id: str, new_car_id: str):

        async with self.db_session as session:

            car = await session.get(CarORM, car_id)
            if car:
                car.car_id = new_car_id
                await session.commit()
                print(car_id, "updated")
                return True
            else:
                print(car_id, "not updated")
                return False

    # Обновление владельца авто

    async def update_car_owner_db(self, car_id: str, new_owner_id: int):
        async with self.db_session as session:
            car = await session.get(CarORM, car_id)

            if car.car_owner == new_owner_id:
                print(car_id, "not changed")
                return car.car_owner

            if car:
                car.car_owner = new_owner_id
                await session.commit()
                print(f"{car_id} owner changed {new_owner_id}")
                return True
            else:
                print({car_id}, "not found")
                return False

    async def show_cars_db(self):
        async with self.db_session as session:
            query = select(CarORM)
            res = await session.execute(query)
            cars = res.scalars().all()
            return cars
