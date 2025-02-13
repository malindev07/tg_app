from dataclasses import dataclass, asdict, field

from car_feature.car_model.car_py_model.car_create_model import CarCreate
from car_feature.car_model.car_py_model.car_py_model import (
    Car,
    CarId,
    CarBrandModel,
    CarVIN,
)
from car_feature.car_model.car_validator.car_validator import CarValidator


@dataclass
class CarAction:
    @staticmethod
    async def create_car(new_car: CarCreate) -> Car | bool:

        if CarValidator.validate_car_id(car_id=new_car.car_id):
            car_id = CarId(car_id=new_car.car_id)
        else:
            return False

        if CarValidator.validate_car_vin(car_vin=new_car.car_vin):
            car_vin = CarVIN(car_vin=new_car.car_vin)
        else:
            return False

        car_brand_model = CarBrandModel(
            car_brand=new_car.car_brand, car_model=new_car.car_model
        )
        car_owner = new_car.car_owner

        car = Car(
            car_id=car_id,
            car_brand_model=car_brand_model,
            car_owner=car_owner,
            car_vin=car_vin,
        )

        return car

    @staticmethod
    async def search_car(car_id: CarId):
        pass

    #
    # @staticmethod
    # def show_cars():
    #     return cars_storage.car_storage
