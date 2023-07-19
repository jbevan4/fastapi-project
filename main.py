import os

from config import Config
from fastapi import FastAPI
from fastapi_project.repositories.database import init_db
from fastapi_project.routes import (
    orders,
)

app = FastAPI()


@app.on_event("startup")
async def on_startup() -> None:
    init_db()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    os.remove(Config.DATABASE_NAME)


app.include_router(orders.router)
