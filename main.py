import uvicorn
from fastapi import FastAPI
from dataclasses import dataclass
from api.health_check import health_router
from contextlib import asynccontextmanager
from api.cars.handlers.car_handler import car_router
from services.car_services.converter.car_converter import CarConverter
from services.car_services.services import CarServices
from repository.car_repository.repository import CarRepository
from services.car_services.validator.car_validator import CarValidator


@asynccontextmanager
async def lifespan(app: FastAPI):
    car_repository = CarRepository()
    car_validator = CarValidator()
    car_converter = CarConverter()
    car_services = CarServices(
        repository=car_repository, validator=car_validator, converter=car_converter
    )

    yield {"car_services": car_services}


app = FastAPI(lifespan=lifespan)


app.include_router(car_router)
app.include_router(health_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
