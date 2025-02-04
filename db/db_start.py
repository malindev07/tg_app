# import asyncio
#
# from db.db_actions.db_car_actions.db_car_action import DataBaseCarAction
# from db.db_models.db_car_model import CarORM
# from db.db_models.db_car_model.db_car_model import CarBase
# from db.db_settings.db_settings import settings
# from db.db_settings.db_helper import DataBaseHelper

# db_helper = DataBaseHelper()


# async def start_db():
#
#     await db_helper.set_engine(url=settings.database_url)
#     await db_helper.set_session_factory()
#     # await db_helper.init_db(CarBase)
#
#     car = CarORM(car_id="O222OO77", car_brand=" BMW")
#
#     await DataBaseCarAction.save_car(car=car, session_factory=db_helper.session_factory)
#     await DataBaseCarAction.search_car(
#         car_id="O222OO777", session_factory=db_helper.session_factory
#     )
#
#
# asyncio.run(start_db())
