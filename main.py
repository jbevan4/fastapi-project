from fastapi import FastAPI
from fastapi_project.routes import (
    orders,
)  # Assuming orders.py is in the routes directory

app = FastAPI()

app.include_router(orders.router)
