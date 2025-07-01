from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class IDNotFoundSchema(BaseModel):
    id_: UUID
    msg: str = Field(default="Not found")


class KeyValueNotFoundSchema(BaseModel):
    data: dict[str, str]
    msg: str = Field(default="Not found")


class ValidationInfoSchema(BaseModel):
    name: str = Field(default="")
    data: list[Any] = Field(default=[])
