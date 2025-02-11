from fastapi import APIRouter

from car_feature.car_actions_router.car_route_actions import CarActionsRouter
from car_feature.car_model.car_api_model.car_api_model import (
    CarCreateAPI,
    CarReturnAPI,
    CarIDApi,
)

car_router = APIRouter(prefix="/car_orm", tags=["Car"])


@car_router.post("/create_car")
async def create_car(new_car: CarCreateAPI) -> CarReturnAPI | bool:
    res = await CarActionsRouter.create_car(new_car=new_car)
    return res


@car_router.post("/search_car")
async def search_car(car_id: CarIDApi):
    res = CarActionsRouter.search_car(car_id=car_id)
    return res


@car_router.get("/show_Cars")
async def show_cars():
    res = CarActionsRouter.show_cars()
    return res
