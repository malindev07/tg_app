import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from core.db.models.base import Base


class CustomerModel(Base):
    __tablename__ = "customers"
    
    id: Mapped[UUID] = mapped_column(primary_key = True, default = uuid.uuid4)
    first_name: Mapped[str] = mapped_column(nullable = False, unique = True)
    last_name: Mapped[str] = mapped_column(nullable = False)
    middle_name: Mapped[str] = mapped_column(nullable = True)
    phone: Mapped[str] = mapped_column(nullable = False, unique = True)
    is_verify: Mapped[bool] = mapped_column(nullable = True)
    tg_id: Mapped[str] = mapped_column(nullable = True)
    discount: Mapped[int] = mapped_column(default = 0)
    created_at: Mapped[datetime] = mapped_column(
        server_default = func.now(), nullable = False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default = func.now(), onupdate = func.now(), nullable = False
    )
