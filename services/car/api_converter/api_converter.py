from dataclasses import dataclass

from domain.car_feature.model.api_model.model import (
    CarCreateAPI,
    CarReturnAPI,
    CarIDApi,
)

from domain.car_feature.model.domain_model.model import Car, CarId, CarVIN


@dataclass
class CarConverterApi:

    @staticmethod
    def convert_car_id_from_api(car_id: CarIDApi) -> CarId:
        return CarId(car_id=car_id.car_id)

    @staticmethod
    def convert_from_api(car: CarCreateAPI) -> Car:
        return Car(
            car_id=CarId(car_id=car.car_id),
            car_vin=CarVIN(car_vin=car.car_vin),
            car_owner=car.car_owner,
            car_brand=car.car_brand,
            car_model=car.car_model,
        )

    @staticmethod
    def convert_from_py_to_api(car: Car) -> CarReturnAPI:
        car_api = CarReturnAPI(
            car_id=car.car_id.car_id,
            car_brand=car.car_brand,
            car_model=car.car_model,
            car_owner=car.car_owner,
            car_vin=car.car_vin.car_vin,
        )
        return car_api
