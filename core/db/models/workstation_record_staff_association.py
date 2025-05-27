from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.models import Base


class WorkstationStaffRecordAssociationModel(Base):
    __tablename__ = "workstation_staff_record_association"

    workstation_id: Mapped[UUID] = mapped_column(
        ForeignKey("workstations.id"), primary_key=True, comment="ID станции"
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

    record: Mapped["RecordModel"] = relationship(back_populates="staff_associations")
    staff: Mapped["StaffModel"] = relationship(back_populates="record_associations")
    workstation: Mapped["WorkstationModel"] = relationship(
        back_populates="workstation_associations"
    )
