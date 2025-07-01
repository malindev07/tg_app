import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.models.base import Base


class CarModel(Base):
    __tablename__ = "cars"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    gos_nomer: Mapped[str] = mapped_column(nullable=False, unique=True)
    brand: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    vin: Mapped[str] = mapped_column(nullable=True)
    odometer_registered: Mapped[int] = mapped_column(nullable=False)
    odometer_last: Mapped[int] = mapped_column(nullable=True)
    owner_id: Mapped[UUID] = mapped_column(ForeignKey("customers.id"), nullable=True)
    owner: Mapped["CustomerModel"] = relationship(
        "CustomerModel", back_populates="cars"
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now(), nullable=False
    )
