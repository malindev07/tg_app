import uuid
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from core.db.models.base import Base


class CarModel(Base):
    __tablename__ = "cars"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    gos_nomer: Mapped[str] = mapped_column(nullable=False, unique=True)
    brand: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    vin: Mapped[str] = mapped_column(nullable=True)
