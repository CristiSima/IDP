from mongoengine import Document, connect as _connect
from os import environ

def connect():
    _connect(
        "IDP",
        username=environ.get("MONGO_USER", None),
        password=environ.get("MONGO_PASSWORD", None),
        host=environ.get("MONGO_HOST"),
    )

__all__ = [
    "connect",
]