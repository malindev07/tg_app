import asyncio

from fastapi import FastAPI

from car_feature.car_api.car_handler import car_router
from db.db_actions.db_car_actions.db_car_action import test_search

app = FastAPI()

app.include_router(car_router)


asyncio.run(test_search())
