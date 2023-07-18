from fastapi import FastAPI
from fastapi_project.repositories.database import init_db
from fastapi_project.routes import (
    orders,
)


app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    init_db()


app.include_router(orders.router)
