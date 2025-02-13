from dataclasses import dataclass, asdict

from car_feature.car_actions.car_crud import CarAction
from car_feature.car_api.car_api_converter.api_converter import CarConverter

from car_feature.car_db_converter.car_db_converter import CarDBConverter
from car_feature.car_model.car_api_model.car_api_model import (
    CarCreateAPI,
    CarReturnAPI,
    CarIDApi,
)
from db.db_actions.db_car_actions.db_car_action import DataBaseCarAction


@dataclass
class CarActionsRouter:

    @staticmethod
    async def create_car(new_car: CarCreateAPI) -> CarReturnAPI | bool:

        search_car = await DataBaseCarAction.search_car_db(car_id=new_car.car_id)

        if search_car:
            car = CarDBConverter.convert_db_to_py(car_orm=search_car)

            return CarConverter.convert_from_py_to_api(car=car)

        res_car = await CarAction.create_car(
            new_car=CarConverter.convert_from_api(car=new_car)
        )

        if res_car:
            save_res = await DataBaseCarAction.save_car_db(
                car=CarDBConverter.convert_py_to_db(car=res_car)
            )
            if save_res:
                car = CarConverter.convert_from_py_to_api(car=res_car)
                return car

        return False

    @staticmethod
    async def search_car(car_id: CarIDApi) -> CarReturnAPI | None:

        res = await DataBaseCarAction.search_car_db(car_id=car_id.car_id)

        if res:
            car = CarDBConverter.convert_db_to_py(car_orm=res)
            return CarConverter.convert_from_py_to_api(car=car)

        return res

    #
    @staticmethod
    async def show_cars() -> dict[str, CarReturnAPI]:
        cars_orm = await DataBaseCarAction.show_cars_db()
        all_cars: dict[str, CarReturnAPI] = {}

        for car_orm in cars_orm:
            car = CarDBConverter.convert_db_to_py(car_orm=car_orm)
            car_re = CarConverter.convert_from_py_to_api(car=car)
            all_cars[car_re.car_id] = car_re

        return all_cars
