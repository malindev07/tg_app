from fastapi import APIRouter, Request

from api.records.schema.records import RecordCreateSchema

record_router = APIRouter(prefix = "/record", tags = ["Record"])


@record_router.post("/")
async def create(request: Request, data: RecordCreateSchema):
    return await request.state.records_services.create(schema = data)

#
# @record_router.get("/")
# async def get(request: Request, id_: UUID):
#     return await request.state.customer_services.get(id_=id_)
#
#
# @record_router.delete("/")
# async def delete(request: Request, id_: UUID):
#     return await request.state.customer_services.delete(id_=id_)
#
#
# @record_router.get("/by-{key}/{value}")
# async def get_by_field(request: Request, key: str, value: str):
#     return await request.state.customer_services.get_by_field(key, value)
#
#
# @record_router.patch("/")
# async def patch(request: Request, data: CustomerPatchSchema):
#     return await request.state.customer_services.partial_update(data=data)
