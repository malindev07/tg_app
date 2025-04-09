from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import AsyncGenerator, AsyncIterator
from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only

from api.cars.schemas.schema import CarCreateSchema, CarSchema
from core.db.helper import db_helper
from services.base_service import BaseService
from core.db.generics import SchemaType
from core.db.models import CarModel
from repository.car_repository.repository import CarRepository


@dataclass
class CarServices(BaseService):
    MODEL = CarModel
    SCHEMA = CarSchema
    repository: CarRepository

    async def create(self, schema: CarCreateSchema) -> SchemaType:
        model = await super()._to_model(schema)  # из pydantic схемы в модель
        obj = await self.repository.create(model=model)
        return await super()._to_schema(obj)  # из модели в схему pydantic

    async def get(self, id_: UUID) -> SchemaType:
        return self._to_schema(await self.repository.get(id_=id_))

    def _to_schema(self, obj: MODEL) -> SCHEMA:
        """Конвертирует модель в схему"""
        return self.SCHEMA.model_validate(obj, from_attributes=True)

    def _to_model(self, data: SCHEMA) -> MODEL:
        """Конвертирует схему в модель"""
        return self.MODEL(**data.model_dump())
