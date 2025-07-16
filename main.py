from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.cars.handler import car_router
from api.customers.handler import customer_router
from api.health_check import health_router
from api.records.handler import record_router
from api.staff.handler import staff_router
from api.workstations.handler import workstation_router
from repository.car_repository.repository import CarRepository
from repository.customers_repository.repository import CustomerRepository
from repository.records_repository.repository import RecordsRepository
from repository.staff_repository.repository import StaffRepository
from repository.workstation_repository.repository import WorkstationRepository
from services.car_services.converter import CarConverter
from services.car_services.services import CarServices
from services.car_services.validator import CarValidator
from services.customer_services.converter import CustomerConverter
from services.customer_services.services import CustomerServices
from services.customer_services.validator import CustomerValidator
from services.records_services.converter import RecordConverter
from services.records_services.services import RecordsServices
from services.records_services.validator import RecordValidator
from services.staff_services.converter import StaffConverter
from services.staff_services.services import StaffServices
from services.staff_services.validator import StaffValidator
from services.workstation_services.converter import WorkstationConverter
from services.workstation_services.services import WorkstationServices


@asynccontextmanager
async def lifespan(app: FastAPI):
    car_services = CarServices(
        repository=CarRepository(),
        validator=CarValidator(),
        converter=CarConverter(),
    )
    customer_services = CustomerServices(
        repository=CustomerRepository(),
        validator=CustomerValidator(),
        converter=CustomerConverter(),
    )
    records_services = RecordsServices(
        repository=RecordsRepository(),
        converter=RecordConverter(),
        validator=RecordValidator(),
    )
    staff_services = StaffServices(
        repository=StaffRepository(),
        converter=StaffConverter(),
        validator=StaffValidator(),
    )
    workstation_services = WorkstationServices(
        repository=WorkstationRepository(),
        converter=WorkstationConverter(),
    )

    yield {
        "car_services": car_services,
        "customer_services": customer_services,
        "records_services": records_services,
        "staff_services": staff_services,
        "workstation_services": workstation_services,
    }


app = FastAPI(lifespan=lifespan)


app.include_router(car_router)
app.include_router(customer_router)
app.include_router(record_router)
app.include_router(staff_router)
app.include_router(workstation_router)

app.include_router(health_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
