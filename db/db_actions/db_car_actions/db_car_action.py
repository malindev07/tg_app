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

                print(f"Авто с гос номером {car.car_id} сохранен в БД")
                return True

        except IntegrityError:
            print(f"Автомобиль с гос номером {car.car_id} уже есть в БД")
            return False

    # Поиск авто по гос номеру
    @staticmethod
    async def search_car_db(car_id: str) -> CarORM | None:
        try:
            async with db_helper.session_factory() as session:

                car = await session.get(CarORM, car_id)
                print(f"Автомобиль с гос номером {car.car_id} найден!")
                return car

        except AttributeError:
            print(f"Автомобиль с гос номером {car_id} не найден")
            return None

    # Обновление гос номера авто
    @staticmethod
    async def update_car_id_db(car_id: str, new_car_id: str):
        async with db_helper.session_factory() as session:
            car = await session.get(CarORM, car_id)
            if car:
                car.car_id = new_car_id
                await session.commit()
                print(f"Гос номер {car_id} изменен на {new_car_id}")
                return True
            else:
                print(f"Автомобиль с гос номером {car_id} не найден")
                return False

    # Обновление владельца авто
    @staticmethod
    async def update_car_owner_db(car_id: str, new_owner_id: int):
        async with db_helper.session_factory() as session:
            car = await session.get(CarORM, car_id)

            if car.car_owner == new_owner_id:
                print("Владелец не сменился")
                return car.car_owner

            if car:
                car.car_owner = new_owner_id
                await session.commit()
                print(f"Владелец {car_id} изменен на {new_owner_id}")
                return True
            else:
                print(f"Автомобиль с гос номером {car_id} не найден")
                return False

    @staticmethod
    async def show_cars_db():
        async with db_helper.session_factory() as session:
            query = select(CarORM)
            res = await session.execute(query)
            cars = res.scalars().all()
            return cars


async def test_search():
    await DataBaseCarAction.show_cars_db()
    await DataBaseCarAction.save_car_db(
        car=CarORM(car_id="А113АА777", car_brand="Volvo")
    )

    await DataBaseCarAction.search_car_db(car_id="А111АА777")

    await DataBaseCarAction.update_car_id_db(car_id="А151АА777", new_car_id="А111АА777")
    await DataBaseCarAction.update_car_owner_db(car_id="А111АА777", new_owner_id=5)
