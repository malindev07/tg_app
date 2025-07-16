from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from core.db.models import Base


class RecordStaffAssociationModel(Base):
    """Ассоциативная таблица для связи многие-ко-многим между записями и сотрудниками"""

    __tablename__ = "record_staff_association"

    record_id: Mapped[UUID] = mapped_column(
        ForeignKey("records.id"), primary_key=True, comment="ID записи"
    )
    staff_id: Mapped[UUID] = mapped_column(
        ForeignKey("staff.id"), primary_key=True, comment="ID сотрудника"
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # # Опциональные отношения для удобства доступа
    # record: Mapped["RecordModel"] = relationship(back_populates="staff_associations")
    # staff: Mapped["StaffModel"] = relationship(back_populates="record_associations")
