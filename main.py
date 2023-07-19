from config import Config
from fastapi import FastAPI
from fastapi_project.repositories.database import cleanup_db, init_db
from fastapi_project.repositories.factory import RepositoryType
from fastapi_project.routes import (
    orders,
)

app = FastAPI()


@app.on_event("startup")
async def on_startup() -> None:
    if Config.REPOSITORY_TYPE == RepositoryType.SQLITE:
        init_db()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    if Config.REPOSITORY_TYPE == RepositoryType.SQLITE:
        cleanup_db()


app.include_router(orders.router)
