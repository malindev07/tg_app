from dataclasses import dataclass, field

from domain.car_feature.actions.crud import CarAction

from domain.car_feature.api.api_model.model import (
    CarCreateAPI,
    CarReturnAPI,
    CarIDApi,
    CarNewIdOwnerAPI,
)
from repository.db.actions.car_actions.car_action import DataBaseCarAction
from services.car.api_converter.api_converter import CarConverter
from services.car.db_converter.car_db_converter import CarDBConverter


@dataclass
class CarActionsRouter:
    car_action: CarAction = CarAction
    car_db_action: DataBaseCarAction = field(default_factory=DataBaseCarAction)

    async def create_car(self, new_car: CarCreateAPI) -> CarReturnAPI | None:

        search_car = await self.car_db_action.search_car_db(car_id=new_car.car_id)

        if search_car:
            car = CarDBConverter.convert_db_to_py(car_orm=search_car)

            return CarConverter.convert_from_py_to_api(car=car)

        car_converted = CarConverter.convert_from_api(car=new_car)

        res_car = await self.car_action(car=car_converted).create_car()

        if res_car:
            save_res = await self.car_db_action.save_car_db(
                car=CarDBConverter.convert_py_to_db(car=res_car)
            )
            if save_res:
                car = CarConverter.convert_from_py_to_api(car=res_car)
                return car

        return None

    async def search_car(self, car_id: CarIDApi) -> CarReturnAPI | None:

        res = await self.car_db_action.search_car_db(car_id=car_id.car_id)

        if res:
            car = CarDBConverter.convert_db_to_py(car_orm=res)
            return CarConverter.convert_from_py_to_api(car=car)

        return res

    async def show_cars(self) -> dict[str, CarReturnAPI]:
        cars_orm = await self.car_db_action.show_cars_db()
        all_cars: dict[str, CarReturnAPI] = {}

        for car_orm in cars_orm:
            car = CarDBConverter.convert_db_to_py(car_orm=car_orm)
            car_re = CarConverter.convert_from_py_to_api(car=car)
            all_cars[car_re.car_id] = car_re

        return all_cars

    async def update_id_and_owner(
        self, car_id: CarIDApi, new_id_owner: CarNewIdOwnerAPI
    ):

        res = await self.car_db_action.update_id_and_owner(
            car_id=car_id.car_id,
            new_car_id=new_id_owner.id,
            new_owner_id=new_id_owner.owner,
        )
        if res:
            car = CarDBConverter.convert_db_to_py(res)
            car_re = CarConverter.convert_from_py_to_api(car)
            return car_re

        return res
