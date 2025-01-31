from fastapi import FastAPI

from car_feature.car_api.car_handler import car_router

app = FastAPI()

app.include_router(car_router)
