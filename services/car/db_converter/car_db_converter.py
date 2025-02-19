from dataclasses import dataclass

from domain.car_feature.model.base_model.model import (
    Car,
    CarId,
    CarBrandModel,
    CarVIN,
)
from repository.db.models.car_model import CarORM


@dataclass
class CarDBConverter:

    @staticmethod
    def convert_py_to_db(car: Car) -> CarORM:
        return CarORM(
            car_id=car.car_id.car_id,
            car_brand=car.car_brand_model.car_brand,
            car_model=car.car_brand_model.car_model,
            car_owner=car.car_owner,
            car_vin=car.car_vin.car_vin,
        )

    @staticmethod
    def convert_db_to_py(car_orm: CarORM) -> Car:
        car_id = CarId(car_id=car_orm.car_id)

        car_brand_model = CarBrandModel(
            car_brand=car_orm.car_brand, car_model=car_orm.car_model
        )

        car_vin = CarVIN(car_vin=car_orm.car_vin)

        return Car(
            car_id=car_id,
            car_brand_model=car_brand_model,
            car_owner=car_orm.car_owner,
            car_vin=car_vin,
        )
