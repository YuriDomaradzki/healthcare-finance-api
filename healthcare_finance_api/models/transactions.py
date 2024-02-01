import uuid

from healthcare_finance_api.models.db import db
from healthcare_finance_api.utils import format_date


class TransactionsModel(db.Model):

    __tablename__ = "transactions"

    UUID = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    AMOUNT = db.Column(db.Numeric, nullable=False)
    TIMESTAMP = db.Column(db.DateTime, nullable=False)

    PATIENT_UUID = db.Column(
        db.String, db.ForeignKey("patients.UUID"), unique=False, nullable=False
    )
    PHARMACY_UUID = db.Column(
        db.String, db.ForeignKey("pharmacies.UUID"), unique=False, nullable=False
    )

    patient = db.relationship("PatientModel", back_populates="transactions")
    pharmacy = db.relationship("PharmacyModel", back_populates="transactions")

    def as_dict(self):
        return {
            "ID": self.UUID,
            "AMOUNT": f"R$ {round(self.AMOUNT, 2)}",
            "TRANSACTION DATE": format_date(date=self.TIMESTAMP, format="%Y-%m-%d"),
            "PATIENT": self.patient.as_dict(),
            "PHARMACY": self.pharmacy.as_dict(),
        }
