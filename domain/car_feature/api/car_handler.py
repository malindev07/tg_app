from dataclasses import asdict

from fastapi import APIRouter, Request, Response


from domain.car_feature.model.api_model.model import (
    CarCreateAPI,
    CarReturnAPI,
)
from services.car.api_converter.api_converter import CarConverterApi
from services.car.validator.car_validator import CarValidator

car_router = APIRouter(prefix="/car", tags=["Car"])


@car_router.post("/create_car")
async def create_car(
    request: Request, response: Response, new_car: CarCreateAPI
) -> CarReturnAPI | dict[str, str] | None:
    is_valid_data = CarValidator(
        car_vin=new_car.car_vin, car_id=new_car.car_id
    ).is_validate()

    if is_valid_data is True:
        car = request.state.car_converter_api.convert_from_api(new_car)

        res = await request.state.car_services.create_car(new_car=car)

        if res is not None:
            car_api = CarConverterApi.convert_from_py_to_api(res)
            return car_api
        else:
            return {new_car.car_id: "registered"}

    return None


# @car_router.post("/create_car")
# async def create_car(req: Request, new_car: CarCreateAPI) -> CarReturnAPI | ValueError:
#     res_valid = CarValidator().validate_car_id(
#         new_car.car_id
#     ) and CarValidator().validate_car_vin(new_car.car_vin)
#
#     if res_valid is True:
#         car = CarConverter.convert_from_api(new_car)
#     else:
#         return res_valid
#
#     res = await req.state.CarAction(converted_car)
#     res = await req.state.car_action_router.create_car(new_car=new_car)
#     return res


# @car_router.post("/search_car")
# async def search_car(req: Request, car_id: CarIDApi) -> CarReturnAPI | None:
#     res = await req.state.car_action_router.search_car(car_id=car_id)
#
#     return res
#
#
# @car_router.get("/show_Cars")
# async def show_cars(req: Request) -> dict[str, CarReturnAPI]:
#     res = await req.state.car_action_router.show_cars()
#     return res
#
#
# @car_router.patch("/update_owner")
# async def update_id_and_owner(
#     req: Request, car_id: CarIDApi, new_id_owner: CarNewIdOwnerAPI
# ):
#
#     res = await req.state.car_action_router.update_id_and_owner(
#         car_id=car_id, new_id_owner=new_id_owner
#     )
#
#     return res
