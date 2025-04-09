from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.cars.handlers.car_handler import car_router
from api.health_check import health_router
from repository.car_repository.repository import CarRepository
from services.car_services.services import CarServices


@asynccontextmanager
async def lifespan(app: FastAPI):
    car_repository = CarRepository()
    car_services = CarServices(repository=car_repository)

    yield {"car_services": car_services}


app = FastAPI(lifespan=lifespan)

app.include_router(car_router)
app.include_router(health_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
