from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class CarBase(DeclarativeBase):
    pass


class CarORM(CarBase):
    __tablename__ = "cars"

    car_id: Mapped[str] = mapped_column(primary_key=True)
    car_brand: Mapped[str]
    car_model: Mapped[str] = mapped_column(nullable=True)
    car_owner: Mapped[int] = mapped_column(nullable=True)
    car_vin: Mapped[str] = mapped_column(nullable=True)
    record_ids: Mapped[int] = mapped_column(nullable=True)
