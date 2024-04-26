from sqlalchemy import func, and_

from flask import request

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from healthcare_finance_api.models import TransactionsModel, PharmacyModel, PatientModel
from healthcare_finance_api.utils import (
    string_validation,
    string_date_validation,
    string_amount_validation,
)


blp = Blueprint("Transactions", __name__, description="Operations on transactions")


@blp.route("/transactions")
class Transcations(MethodView):

    @jwt_required()
    def get(self):

        patient_name = request.args.get('patient_name')
        patient_last_name = request.args.get('patient_last_name')
        date = request.args.get('date')
        end_date = request.args.get('end_date')
        min_value = request.args.get('min_value')
        max_value = request.args.get('max_value')
        pharmacy_name = request.args.get('pharmacy_name')

        try:
            if patient_name and patient_last_name:
                if not string_validation(text=patient_name) or not string_validation(
                    text=patient_last_name
                ):
                    raise ValueError(
                        "The patient's first or last name entered "
                        "for the query is in an invalid format!"
                    )
                transactions = [
                    transaction.as_dict()
                    for transaction in TransactionsModel.query.join(
                        TransactionsModel.patient
                    )
                    .filter(
                        PatientModel.FIRST_NAME == patient_name.upper(),
                        PatientModel.LAST_NAME == patient_last_name.upper(),
                    )
                    .order_by(TransactionsModel.TIMESTAMP)
                    .all()
                ]
            elif min_value and max_value:
                if not string_amount_validation(
                    amount=min_value
                ) or not string_amount_validation(amount=max_value):
                    raise ValueError(
                        "The minimum or maximum value of the transactions entered in the "
                        "query is in an invalid format!"
                    )

                min_value = round(float(min_value), 2)
                max_value = round(float(max_value), 2)

                transactions = [
                    transaction.as_dict()
                    for transaction in TransactionsModel.query.filter(
                        TransactionsModel.AMOUNT.between(min_value, max_value)
                    )
                    .order_by(TransactionsModel.TIMESTAMP, TransactionsModel.AMOUNT)
                    .all()
                ]
            elif date and end_date:
                if not string_date_validation(date=date) or not string_date_validation(
                    date=end_date
                ):
                    raise ValueError(
                        "The transactions' start or end date entered for the "
                        "query is in an invalid format!"
                    )

                transactions = [
                    transaction.as_dict()
                    for transaction in TransactionsModel.query.filter(
                        and_(
                            date <= func.date(TransactionsModel.TIMESTAMP),
                            func.date(TransactionsModel.TIMESTAMP) <= end_date,
                        )
                    )
                    .order_by(TransactionsModel.TIMESTAMP)
                    .all()
                ]
            elif pharmacy_name and date:
                if not string_date_validation(date=date) or not string_validation(text=pharmacy_name):
                    raise ValueError(
                        "The pharmacy name or transaction date entered for"
                        " the query is in an invalid format!"
                    )

                transactions = [
                    transaction.as_dict()
                    for transaction in TransactionsModel.query.join(
                        TransactionsModel.pharmacy
                    )
                    .filter(
                        PharmacyModel.NAME == pharmacy_name.upper(),
                        func.date(TransactionsModel.TIMESTAMP) == date,
                    )
                    .order_by(TransactionsModel.TIMESTAMP)
                    .all()
                ]
            elif pharmacy_name:
                if not string_validation(text=pharmacy_name):
                    raise ValueError(
                        "The pharmacy name entered for the query is in an invalid format!"
                    )

                transactions = [
                    transaction.as_dict()
                    for transaction in TransactionsModel.query.join(
                        TransactionsModel.pharmacy
                    )
                    .filter(PharmacyModel.NAME == pharmacy_name.upper())
                    .order_by(PharmacyModel.UUID, TransactionsModel.TIMESTAMP)
                    .all()
                ]
            else:
                transactions = [
                    transaction.as_dict()
                    for transaction in TransactionsModel.query.order_by(
                        TransactionsModel.TIMESTAMP
                    ).all()
                ]

            if not transactions:
                raise LookupError(f"No transactions found for the search!")
            return {"Transactions": transactions}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")

