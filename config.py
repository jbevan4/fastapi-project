import os

from fastapi_project.repositories.types import RepositoryType


class Config:
    DEBUG = os.getenv("DEBUG", False)
    DATABASE_NAME = "default.db"
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_NAME}")
    REPOSITORY_TYPE = RepositoryType[os.getenv("REPOSITORY_TYPE", "IN_MEMORY")]
