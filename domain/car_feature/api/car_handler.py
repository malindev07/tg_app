from fastapi import APIRouter, Request


from domain.car_feature.api.api_model.model import (
    CarCreateAPI,
    CarReturnAPI,
    CarIDApi,
    CarNewIdOwnerAPI,
)

car_router = APIRouter(prefix="/car_orm", tags=["Car"])


@car_router.post("/create_car")
async def create_car(req: Request, new_car: CarCreateAPI) -> CarReturnAPI | None:

    res = await req.state.car_action_router.create_car(new_car=new_car)
    return res


@car_router.post("/search_car")
async def search_car(req: Request, car_id: CarIDApi) -> CarReturnAPI | None:
    res = await req.state.car_action_router.search_car(car_id=car_id)

    return res


@car_router.get("/show_Cars")
async def show_cars(req: Request) -> dict[str, CarReturnAPI]:
    res = await req.state.car_action_router.show_cars()
    return res


@car_router.patch("/update_owner")
async def update_id_and_owner(
    req: Request, car_id: CarIDApi, new_id_owner: CarNewIdOwnerAPI
):

    res = await req.state.car_action_router.update_id_and_owner(
        car_id=car_id, new_id_owner=new_id_owner
    )

    return res
