from dataclasses import dataclass

from domain.car_feature.model.base_model.create_model import CarCreate
from domain.car_feature.model.base_model.model import (
    Car,
    CarId,
    CarBrandModel,
    CarVIN,
)
from services.car.validator.car_validator import CarValidator


@dataclass
class CarAction:
    car: CarCreate

    async def create_car(self) -> Car | None:

        if CarValidator.validate_car_id(car_id=self.car.car_id):
            car_id = CarId(car_id=self.car.car_id)
        else:
            return None

        if CarValidator.validate_car_vin(car_vin=self.car.car_vin):
            car_vin = CarVIN(car_vin=self.car.car_vin)
        else:
            return None

        car_brand_model = CarBrandModel(
            car_brand=self.car.car_brand, car_model=self.car.car_model
        )
        car_owner = self.car.car_owner

        car = Car(
            car_id=car_id,
            car_brand_model=car_brand_model,
            car_owner=car_owner,
            car_vin=car_vin,
        )

        return car
