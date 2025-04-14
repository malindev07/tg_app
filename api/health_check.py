from dataclasses import asdict

from fastapi import APIRouter, Request, Response, Depends


from sqlalchemy.ext.asyncio import AsyncSession

from core.db.helper import db_helper

health_router = APIRouter(prefix="/health_check", tags=["Health Check"])


@health_router.get("/db_health")
async def create(session: AsyncSession = Depends(db_helper.session)):
    return await db_helper.health_check()
