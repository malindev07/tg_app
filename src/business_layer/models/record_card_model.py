from dataclasses import dataclass, field


@dataclass
class ClientRecordCard:

    client_car: str
    visit_reason: str
    record_time: str
    record_date: str
    client_name: str = field(default_factory=str)
    client_phone: str = field(default_factory=str)

    def change_record_time(self, new_time: str) -> None:
        self.record_time = new_time

    def change_record_date(self, new_date: str) -> None:
        self.record_date = new_date

    def change_client_car(self, changed_car: str) -> None:
        self.client_car = changed_car

    def change_client_name(self, changed_name: str) -> None:
        self.client_name = changed_name

    def change_client_phone(self, changed_phone: str) -> None:
        self.client_name = changed_phone
