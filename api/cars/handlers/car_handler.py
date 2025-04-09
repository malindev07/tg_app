from uuid import UUID

from fastapi import APIRouter, Request, Depends


from sqlalchemy.ext.asyncio import AsyncSession

from api.cars.schemas.schema import CarCreateSchema
from core.db.helper import db_helper
from services.car_services.services import CarServices

car_router = APIRouter(prefix="/car", tags=["Car"])


@car_router.post("/")
async def create(
    request: Request,
    data: CarCreateSchema,
):
    return await request.state.car_services.create(data)


@car_router.get("/{id_}")
async def get(
    request: Request,
    id_: UUID,
):
    return await request.state.car_services.get(id_)
