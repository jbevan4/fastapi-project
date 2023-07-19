import os


class Config:
    DEBUG = os.getenv("DEBUG", False)
    DATABASE_NAME = "default.db"
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_NAME}")
    REPOSITORY_TYPE = os.getenv("REPOSITORY_TYPE", "in_memory")
