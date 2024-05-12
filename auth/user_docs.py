from mongoengine import Document, connect as _connect
from mongoengine.fields import StringField, BooleanField
from os import environ
from hashlib import sha256


__all__ = [
    "connect",
    "UserDocument",
    "makePassHash"
]

def connect():
    _connect(
        "IDP",
        username=environ.get("MONGO_USER", None),
        password=environ.get("MONGO_PASSWORD", None),
        host=environ.get("MONGO_HOST"),
    )

def makePassHash(passw):
    salt = "most_epic_salt_you_have_seen_ngl"
    return sha256((salt + passw).encode("utf-8")).hexdigest()

class UserDocument(Document):
    username = StringField(required = True)
    passw = StringField(required = True)

    def __repr__(self):
        return f"UserDocument<{self.username} @{self.passw}>"