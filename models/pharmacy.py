import uuid
from db import db


class PharmacyModel(db.Model):

    __tablename__ = "pharmacies"

    UUID = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    NAME = db.Column(db.String, nullable=False)
    CITY = db.Column(db.String, nullable=False)

    transactions = db.relationship("TransactionsModel", back_populates="pharmacy")

    def as_dict(self):
        return {
            "ID": self.UUID,
            "NAME": self.NAME,
            "CITY": self.CITY,
        }

