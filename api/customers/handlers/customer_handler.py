from fastapi import APIRouter
from requests import Request

from api.customers.schemas.customer import CreateCustomerSchema

customer_router = APIRouter(prefix="/customer", tags=["Customer"])


@customer_router.post("/")
async def create(request: Request, data: CreateCustomerSchema):
    pass
