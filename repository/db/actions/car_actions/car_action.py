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
    async def save_car_db(self, car: CarORM) -> CarORM | None:
        try:
            async with self.db_session as session:
                session.add(car)
                await session.commit()
                print(car.car_id, "saved")
                return car

        except IntegrityError:
            print(car.car_id, "not saved")
            return None

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

    async def update_id_and_owner(
        self, car_id: str, new_car_id: str = None, new_owner_id: int = None
    ):

        async with self.db_session as session:
            car = await session.get(CarORM, car_id)
            if car:
                if new_car_id:
                    car.car_id = new_car_id
                if new_owner_id:
                    car.car_owner = new_owner_id

                await session.commit()
                print(car_id, "updated")
                return car
            else:
                print(car_id, "not found")
                return None

    #
    # # Обновление гос номера авто
    # async def update_car_id_db(self, car_id: str, new_car_id: str) -> CarORM | None:
    #
    #     async with self.db_session as session:
    #
    #         car = await session.get(CarORM, car_id)
    #         if car:
    #             car.car_id = new_car_id
    #             await session.commit()
    #             print(car_id, "updated")
    #             return car
    #         else:
    #             print(car_id, "not updated")
    #             return None
    #
    # # Обновление владельца авто
    # async def update_car_owner_db(
    #     self, car_id: str, new_owner_id: int
    # ) -> CarORM | None:
    #     async with self.db_session as session:
    #         car = await session.get(CarORM, car_id)
    #
    #         if car.car_owner == new_owner_id:
    #             print(car_id, "not changed")
    #             return car
    #
    #         if car:
    #             car.car_owner = new_owner_id
    #             await session.commit()
    #             print(f"{car_id} owner changed {new_owner_id}")
    #             return car
    #
    #         else:
    #             print({car_id}, "not found")
    #             return None

    async def show_cars_db(self):
        async with self.db_session as session:
            query = select(CarORM)
            res = await session.execute(query)
            cars = res.scalars().all()
            return cars
