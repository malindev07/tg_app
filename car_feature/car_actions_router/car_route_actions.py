from dataclasses import dataclass

from car_feature.car_actions.car_crud import CarAction
from car_feature.car_api.car_api_converter.api_converter import CarConverter

from car_feature.car_db_converter.car_db_converter import CarDBConverter
from car_feature.car_model.car_api_model.car_api_model import (
    CarCreateAPI,
    CarReturnAPI,
)
from db.db_actions.db_car_actions.db_car_action import DataBaseCarAction


@dataclass
class CarActionsRouter:

    @staticmethod
    async def create_car(new_car: CarCreateAPI) -> CarReturnAPI | bool:

        search_car = await DataBaseCarAction.search_car_db(car_id=new_car.car_id)

        if search_car:
            car = CarDBConverter.convert_db_to_py(car_orm=search_car)
            print("Такая машинка уже есть в бд")
            return CarConverter.convert_from_py_to_api(car=car)

        res_car = await CarAction.create_car(
            new_car=CarConverter.convert_from_api(car=new_car)
        )
        print("Конвертнули из апи в пай")

        if res_car:
            save_res = await DataBaseCarAction.save_car_db(
                car=CarDBConverter.convert_py_to_db(car=res_car)
            )
            print("Попытались сохранить и ковернутли из пай в дб")

            if save_res:
                car = CarConverter.convert_from_py_to_api(car=res_car)
                print("Попытались сохранить и ковернутли из пай в апи")
                return car

        return False

    # @staticmethod
    # def search_car(car_id: CarIDApi):
    #     car_orm = CarAction.search_car(
    #         car_id=CarConverter.convert_car_id_from_api(car_id=car_id)
    #     )
    #     return car_orm
    #
    # @staticmethod
    # def show_cars():
    #     res = CarAction.show_cars()
    #     return res
