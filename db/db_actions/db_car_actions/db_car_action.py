from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from db.db_models.db_car_model import CarORM
from db.db_settings.db_helper import db_helper


@dataclass
class DataBaseCarAction:

    # Сохранение авто в бд
    @staticmethod
    async def save_car_db(car: CarORM) -> CarORM | bool:
        try:
            async with db_helper.session_factory() as session:
                session.add(car)
                await session.commit()
                print(car.car_id, "saved")
                return True

        except IntegrityError:
            print(car.car_id, "not saved")
            return False

    # Поиск авто по гос номеру
    @staticmethod
    async def search_car_db(car_id: str) -> CarORM | None:
        try:
            async with db_helper.session_factory() as session:

                car = await session.get(CarORM, car_id)
                print(car.car_id, "found")
                return car

        except AttributeError:
            print(car_id, "not found")
            return None

    # Обновление гос номера авто
    @staticmethod
    async def update_car_id_db(car_id: str, new_car_id: str):
        async with db_helper.session_factory() as session:
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
    @staticmethod
    async def update_car_owner_db(car_id: str, new_owner_id: int):
        async with db_helper.session_factory() as session:
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

    @staticmethod
    async def show_cars_db():
        async with db_helper.session_factory() as session:
            query = select(CarORM)
            res = await session.execute(query)
            cars = res.scalars().all()
            return cars


# async def test_search():
#     await DataBaseCarAction.show_cars_db()
#     await DataBaseCarAction.save_car_db(
#         car=CarORM(car_id="А113АА777", car_brand="Volvo")
#     )

# await DataBaseCarAction.search_car_db(car_id="А111АА777")
#
# await DataBaseCarAction.update_car_id_db(car_id="А151АА777", new_car_id="А111АА777")
# await DataBaseCarAction.update_car_owner_db(car_id="А111АА777", new_owner_id=5)
