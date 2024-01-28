import uuid
from db import db


class UsersModel(db.Model):

    __tablename__ = "USERS"

    UUID = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    USERNAME = db.Column(db.String, nullable=False)
    PASSWORD = db.Column(db.String, nullable=False)

