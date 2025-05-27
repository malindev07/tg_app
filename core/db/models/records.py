import uuid
from datetime import datetime, date, time
from enum import Enum
from uuid import UUID

from sqlalchemy import func, ForeignKey, String, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.db.models.base import Base


class RecordStatus(Enum):
    CREATED = "Создана"
    IN_PROGRESS = "В работе"
    COMPLETED = "Завершена"
    CANCELLED = "Отменена"


class RecordModel(Base):
    __tablename__ = "records"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    client_id: Mapped[UUID] = mapped_column(ForeignKey("customers.id"), nullable=False)
    car_id: Mapped[UUID] = mapped_column(ForeignKey("cars.id"), nullable=False)

    reason: Mapped[str] = mapped_column(
        String(1000), comment="Причина обращения (макс. 1000 символов)", nullable=False
    )
    status: Mapped[RecordStatus] = mapped_column(
        default=RecordStatus.CREATED, nullable=False
    )
    comment: Mapped[str] = mapped_column(default="", nullable=True)

    record_date: Mapped[date] = mapped_column(Date, nullable=False)

    start_time: Mapped[time] = mapped_column(Time(timezone=True), nullable=False)
    end_time: Mapped[time] = mapped_column(Time(timezone=True), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now(), nullable=False
    )

    staff_associations: Mapped[list["WorkstationStaffRecordAssociationModel"]] = (
        relationship(back_populates="record", cascade="all, delete-orphan")
    )
    workstation_associations: Mapped[list["WorkstationStaffRecordAssociationModel"]] = (
        relationship(back_populates="staff", cascade="all, delete-orphan")
    )
