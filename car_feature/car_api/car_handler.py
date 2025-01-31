from fastapi import APIRouter


from car_feature.car_actions_router.car_route_actions import CarActionsRouter
from car_feature.car_model.car_api_model.car_api_model import CarCreateAPI, CarReturnAPI

car_router = APIRouter(prefix="/car", tags=["Car"])


@car_router.post("/create_car")
async def create_car(new_car: CarCreateAPI) -> CarReturnAPI | bool:
    res = CarActionsRouter.create_car(new_car=new_car)
    return res
