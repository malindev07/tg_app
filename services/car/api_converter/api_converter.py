from dataclasses import dataclass

from domain.car_feature.api.api_model.model import (
    CarCreateAPI,
    CarReturnAPI,
    CarIDApi,
)
from domain.car_feature.model.base_model.create_model import CarCreate
from domain.car_feature.model.base_model.model import Car, CarId


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
            car_vin=car.car_vin.car_vin,
        )
        return car_api
