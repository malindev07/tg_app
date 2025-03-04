from dataclasses import dataclass

from repository.car_repository.car_repository_orm import CarRepositoryORM
from repository.db.models.car_model import CarORM


@dataclass
class CarServicesORM:
    repository: CarRepositoryORM

    async def create_car(self, car: CarORM) -> CarORM | None:
        find_car = await self.repository.find_car_by_id(car_id=car.car_id)

        if find_car:
            return None

        car_orm = await self.repository.create_car(car=car)
        if car_orm:
            return car
