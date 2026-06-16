import os

class Config:

    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://mongo:27017"
    )

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "users_db"
    )