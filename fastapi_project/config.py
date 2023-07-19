import os


class Config:
    DEBUG = os.getenv("DEBUG", False)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")
    REPOSITORY_TYPE = os.getenv("REPOSITORY_TYPE", "in_memory")
