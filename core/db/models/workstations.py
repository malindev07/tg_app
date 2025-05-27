import uuid
from datetime import datetime, time
from enum import Enum
from uuid import UUID

from sqlalchemy import func, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.models.base import Base


class WorkstationTitle(Enum):
    DIAGNOSTIC = "Зона диагностики"
    FAST_TO = "Зона быстрого ТО"
    REPAIR = "Зона ремонта"
    INSTALLATION = "Зона установки"
    LONG_REPAIR = "Зона продолжительного ремонта"


class WorkstationStatus(Enum):
    WORK = "В работе"
    FREE = "Свободна"


class WorkstationModel(Base):
    __tablename__ = "workstations"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[WorkstationTitle] = mapped_column(nullable=False)
    status: Mapped[WorkstationStatus] = mapped_column(
        nullable=False, default=WorkstationStatus.FREE
    )
    description: Mapped[str] = mapped_column(
        nullable=False, default="Описание отсутствует"
    )
    start_time: Mapped[time] = mapped_column(Time(timezone=True), nullable=False)
    end_time: Mapped[time] = mapped_column(Time(timezone=True), nullable=False)

    staff_associations: Mapped[list["WorkstationStaffRecordAssociationModel"]] = (
        relationship(back_populates="record", cascade="all, delete-orphan")
    )
    record_associations: Mapped[list["WorkstationStaffRecordAssociationModel"]] = (
        relationship(back_populates="staff", cascade="all, delete-orphan")
    )
