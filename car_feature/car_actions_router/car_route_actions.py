from dataclasses import dataclass

from car_feature.car_actions.car_crud import CarAction
from car_feature.car_api.car_api_converter.api_converter import CarConverter
from car_feature.car_model.car_api_model.car_api_model import CarCreateAPI, CarReturnAPI


@dataclass
class CarActionsRouter:

    @staticmethod
    def create_car(new_car: CarCreateAPI) -> CarReturnAPI | bool:

        car = CarAction.create_car(new_car=CarConverter.convert_from_api(car=new_car))

        if car:
            res = CarConverter.convert_from_py_to_api(car=car)
            return res

        return False
