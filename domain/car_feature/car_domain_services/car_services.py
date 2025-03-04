from dataclasses import dataclass, asdict

from domain.car_feature.model.domain_model.model import Car
from repository.car_repository.car_services_orm import CarServicesORM
from services.car.db_converter.car_db_converter import CarDBConverter


@dataclass
class CarServices:
    services_orm: CarServicesORM
    converter: CarDBConverter

    async def create_car(self, new_car: Car) -> Car | None:
        car_orm = self.converter.convert_py_to_db(car=new_car)
        res = await self.services_orm.create_car(car=car_orm)

        if res is not None:
            car = self.converter.convert_db_to_py(res)
            return car
        else:
            return None
