from uuid import UUID

from watchfiles import awatch

from core.db.helper import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Request, Depends
from api.cars.schemas.schema import CarCreateSchema

car_router = APIRouter(prefix="/car", tags=["Car"])


@car_router.post("/")
async def create(
    request: Request,
    data: CarCreateSchema,
    session: AsyncSession = Depends(db_helper.session),
):

    return await request.state.car_services.create(schema=data, session=session)


@car_router.get("/{id_}")
async def get(
    request: Request,
    id_: UUID,
    session: AsyncSession = Depends(db_helper.session),
):

    return await request.state.car_services.get(id_=id_, session=session)


@car_router.delete("/{id_}")
async def delete(
    request: Request,
    id_: UUID,
    session: AsyncSession = Depends(db_helper.session),
):
    return await request.state.car_services.delete(id_, session)
