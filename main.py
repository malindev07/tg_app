from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


from domain.car_feature.api.car_handler import car_router
from domain.car_feature.car_domain_services.car_services import CarServices
from repository.car_repository.car_repository_orm import CarRepositoryORM
from repository.car_repository.car_services_orm import CarServicesORM
from repository.db.settings.helper import DataBaseHelper
from repository.db.settings.settings import Settings
from services.car.api_converter.api_converter import CarConverterApi
from services.car.db_converter.car_db_converter import CarDBConverter
from services.car.validator.car_validator import CarValidator


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_helper = DataBaseHelper(db_url=Settings().database_url)
    car_converter_db = CarDBConverter()
    car_converter_api = CarConverterApi()
    car_repository_orm = CarRepositoryORM(session=db_helper.session_factory)
    car_services_orm = CarServicesORM(repository=car_repository_orm)
    car_services = CarServices(
        services_orm=car_services_orm, converter=car_converter_db
    )

    yield {
        "car_converter_db": car_converter_db,
        "car_repository_orm": car_repository_orm,
        "car_services_orm": car_services_orm,
        "car_services": car_services,
        "car_converter_api": car_converter_api,
    }


app = FastAPI(lifespan=lifespan)

app.include_router(car_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
