# import asyncio
from dataclasses import dataclass


from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


from db.db_models.db_car_model import CarORM
# from db.db_settings.db_helper import db_helper


@dataclass
class DataBaseCarAction:

    @staticmethod
    async def save_car(
        car: CarORM, session_factory: async_sessionmaker[AsyncSession]
    ) -> bool:
        try:
            async with session_factory() as session:

                session.add(car)
                await session.commit()

                print(True)
                return True

        except:
            print(False)
            return False

    @staticmethod
    async def search_car(
        car_id: str, session_factory: async_sessionmaker[AsyncSession]
    ):
        try:
            async with session_factory() as session:
                car = await session.get(CarORM, car_id)
                print(car.car_id, car.car_brand)
        except:
            print("Error")


# #
# async def test_search():
#
#     await DataBaseCarAction.search_car(
#         car_id="O222OO77", session_factory=db_helper.session_factory
#     )
