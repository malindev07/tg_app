from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from domain.car_feature.actions_router.router import CarActionsRouter
from domain.car_feature.api.car_handler import car_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    car_action_router = CarActionsRouter()

    yield {"car_action_router": car_action_router}


app = FastAPI(lifespan=lifespan)

app.include_router(car_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
