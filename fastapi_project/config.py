import os


class Config:
    DEBUG = os.getenv("DEBUG", False)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")
