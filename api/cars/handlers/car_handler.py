from dataclasses import asdict
from uuid import UUID

from fastapi import APIRouter, Request, Response, Depends


from sqlalchemy.ext.asyncio import AsyncSession

from api.cars.schemas.schema import CarCreateSchema, CarIDSchema
from apps.services.car_services.services import CarServices
from core.db.helper import db_helper
from repository.car_repository.repository import CarRepository, get_car_repo

car_router = APIRouter(prefix="/car", tags=["Car"])


@car_router.post("/")
async def create(
    request: Request,
    data: CarCreateSchema,
    session: AsyncSession = Depends(db_helper.session),
    car_repo: CarRepository = Depends(get_car_repo),
    car_service: CarServices = Depends(get_car_service),
):

    return await car_repo.create(session, data)


@car_router.get("/{id_}")
async def get(
    id_: UUID,
    session: AsyncSession = Depends(db_helper.session),
    car_repo: CarRepository = Depends(get_car_repo),
):
    return await car_repo.get(session, id_)
