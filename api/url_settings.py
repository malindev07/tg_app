from dataclasses import dataclass


@dataclass
class UrlPrefix:
    car: str = "/car"
    customer: str = "/customer"
    record: str = "/record"
    staff: str = "/staff"
    workstation: str = "/workstation"
