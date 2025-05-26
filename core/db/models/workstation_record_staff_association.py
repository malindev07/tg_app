from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from core.db.models import Base


class WorkstationStaffRecordAssociationModel(Base):
    __tablename__ = "workstation_staff_record_association"

    workstation_id: Mapped[UUID] = mapped_column(
        ForeignKey("workstations.id"), primary_key=True, comment="ID записи"
    )
    record_id: Mapped[UUID] = mapped_column(
        ForeignKey("records.id"), primary_key=True, comment="ID записи"
    )
    staff_id: Mapped[UUID] = mapped_column(
        ForeignKey("staff.id"), primary_key=True, comment="ID сотрудника"
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), comment="Дата и время создания"
    )
    update_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), comment="Дата и время обновления"
    )
