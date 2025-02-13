from dataclasses import dataclass

from car_feature.car_model.car_api_model.car_api_model import (
    CarCreateAPI,
    CarReturnAPI,
    CarIDApi,
)
from car_feature.car_model.car_py_model.car_create_model import CarCreate
from car_feature.car_model.car_py_model.car_py_model import Car, CarId


@dataclass
class CarConverter:

    @staticmethod
    def convert_car_id_from_api(car_id: CarIDApi) -> CarId:
        return CarId(car_id=car_id.car_id)

    @staticmethod
    def convert_from_api(car: CarCreateAPI) -> CarCreate:
        return CarCreate(
            car_id=car.car_id,
            car_vin=car.car_vin,
            car_owner=car.car_owner,
            car_brand=car.car_brand,
            car_model=car.car_model,
        )

    @staticmethod
    def convert_from_py_to_api(car: Car) -> CarReturnAPI:
        car_api = CarReturnAPI(
            car_id=car.car_id.car_id,
            car_brand=car.car_brand_model.car_brand,
            car_model=car.car_brand_model.car_model,
            car_owner=car.car_owner,
        )

        return car_api
