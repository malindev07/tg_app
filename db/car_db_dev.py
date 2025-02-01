from dataclasses import dataclass, field


@dataclass
class CarDB:
    car_storage: dict[str, dict] = field(default_factory=dict)


cars_storage = CarDB()
