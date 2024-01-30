import uuid

from healthcare_finance_api.models.db import db
from healthcare_finance_api.utils import format_date


class PatientModel(db.Model):

    __tablename__ = "patients"

    UUID = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    FIRST_NAME = db.Column(db.String, nullable=False)
    LAST_NAME = db.Column(db.String, nullable=False)
    DATE_OF_BIRTH = db.Column(db.DateTime, nullable=False)

    transactions = db.relationship("TransactionsModel", back_populates="patient")

    def as_dict(self):
        return {
            "ID": self.UUID,
            "FIRST NAME": self.FIRST_NAME,
            "LAST NAME": self.LAST_NAME,
            "DATE OF BIRTH": format_date(date=self.DATE_OF_BIRTH, format="%Y-%m-%d")
        }

