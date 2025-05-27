import uuid
from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.models.base import Base


class StaffRoots(Enum):
    TEST_ROOT = "TEST"


class StaffPosition(Enum):
    SENIOR_MASTER = "Старший мастер"
    MIDDLE_MASTER = "Мастер"
    JUNIOR_MASTER = "Младший мастер"
    TRAINEE = "Стажер"


class StaffStatus(Enum):
    WORK = "Работает"
    VACATION = "В отпуске"
    SICK = "Больничный"
    WEEKEND = "Выходной"
    TRAINEE = "Стажировка"


class StaffModel(Base):
    __tablename__ = "staff"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    position: Mapped[StaffPosition] = mapped_column(default=StaffPosition.MIDDLE_MASTER)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    middle_name: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=False, unique=True)
    status: Mapped[StaffStatus] = mapped_column(
        default=StaffStatus.WORK, nullable=False
    )

    salary_rate: Mapped[float] = mapped_column(nullable=False)

    comment: Mapped[str] = mapped_column(default="", nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now(), nullable=False
    )

    workstation_record_associations: Mapped[
        list["WorkstationStaffRecordAssociationModel"]
    ] = relationship(back_populates="staff", cascade="save-update, merge")
