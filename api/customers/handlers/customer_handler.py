from fastapi import APIRouter, Request

from api.customers.schemas.customer import CreateCustomerSchema
from repository.base_repository import RepositoryORM
from services.customer_services.converter import CustomerConverter
from services.customer_services.saervices import CustomerServices

customer_router = APIRouter(prefix="/customer", tags=["Customer"])


@customer_router.post("/")
async def create(request: Request, data: CreateCustomerSchema):
    c = CustomerServices(repository=RepositoryORM(), converter=CustomerConverter())
    return await c.create(data)
