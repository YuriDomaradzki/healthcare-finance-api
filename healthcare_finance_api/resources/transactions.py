from sqlalchemy import func, and_

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
class Transactions(MethodView):

    @jwt_required()
    def get(self):
        try:
            transactions = [
                transaction.as_dict()
                for transaction in TransactionsModel.query.order_by(
                    TransactionsModel.TIMESTAMP
                ).all()
            ]
            if not transactions:
                raise LookupError(f"No Transactions")
            return {"Transactions": transactions}
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/pharmacy/<string:name>")
class TranscationsByPharmacyName(MethodView):

    @jwt_required()
    def get(self, name: str):
        if not string_validation(text=name):
            raise ValueError(
                "The pharmacy name entered for the query is in an invalid format!"
            )

        try:
            transaction = [
                transaction.as_dict()
                for transaction in TransactionsModel.query.join(
                    TransactionsModel.pharmacy
                )
                .filter(PharmacyModel.NAME == name.upper())
                .order_by(PharmacyModel.UUID, TransactionsModel.TIMESTAMP)
                .all()
            ]
            if not transaction:
                raise LookupError(f"No transactions were found for the pharmacy {name}")
            return {"Transaction": transaction}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/pharmacy/<string:name>/date/<string:date>")
class TranscationsByDate(MethodView):

    @jwt_required()
    def get(self, name: str, date: str):
        if not string_date_validation(date=date) or not string_validation(text=name):
            raise ValueError(
                "The pharmacy name or transaction date entered for"
                " the query is in an invalid format!"
            )

        try:
            transaction = [
                transaction.as_dict()
                for transaction in TransactionsModel.query.join(
                    TransactionsModel.pharmacy
                )
                .filter(
                    PharmacyModel.NAME == name.upper(),
                    func.date(TransactionsModel.TIMESTAMP) == date,
                )
                .order_by(TransactionsModel.TIMESTAMP)
                .all()
            ]
            if not transaction:
                raise LookupError(
                    f"No transactions were found for the " "pharmacy {name} in {date}"
                )
            return {"Transaction": transaction}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/patient/<string:first_name>/<string:last_name>")
class TransactionsByPatientFirstAndLastName(MethodView):

    @jwt_required()
    def get(self, first_name: str, last_name: str):
        if not string_validation(text=first_name) or not string_validation(
            text=last_name
        ):
            raise ValueError(
                "The patient's first or last name entered "
                "for the query is in an invalid format!"
            )

        try:
            transaction = [
                transaction.as_dict()
                for transaction in TransactionsModel.query.join(
                    TransactionsModel.patient
                )
                .filter(
                    PatientModel.FIRST_NAME == first_name.upper(),
                    PatientModel.LAST_NAME == last_name.upper(),
                )
                .order_by(TransactionsModel.TIMESTAMP)
                .all()
            ]
            if not transaction:
                raise LookupError(
                    "No transactions were found for the patient"
                    f" {first_name} {last_name}"
                )
            return {"Transaction": transaction}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/byPeriod/<string:start_date>/<string:end_date>")
class TransactionsByPeriod(MethodView):

    @jwt_required()
    def get(self, start_date: str, end_date: str):
        if not string_date_validation(date=start_date) or not string_date_validation(
            date=end_date
        ):
            raise ValueError(
                "The transactions' start or end date entered for the "
                "query is in an invalid format!"
            )

        try:
            transaction = [
                transaction.as_dict()
                for transaction in TransactionsModel.query.filter(
                    and_(
                        start_date <= func.date(TransactionsModel.TIMESTAMP),
                        func.date(TransactionsModel.TIMESTAMP) <= end_date,
                    )
                )
                .order_by(TransactionsModel.TIMESTAMP)
                .all()
            ]
            if not transaction:
                raise LookupError(
                    "No transactions were found for in the "
                    f"period from {start_date} to {end_date}"
                )
            return {"Transaction": transaction}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/byValues/<string:min_value>/<string:max_value>")
class TransactionsByValues(MethodView):

    @jwt_required()
    def get(self, min_value: str, max_value: str):
        if not string_amount_validation(
            amount=min_value
        ) or not string_amount_validation(amount=max_value):
            raise ValueError(
                "The minimum or maximum value of the transactions entered in the "
                "query is in an invalid format!"
            )

        min_value = round(float(min_value), 2)
        max_value = round(float(max_value), 2)

        try:
            transaction = [
                transaction.as_dict()
                for transaction in TransactionsModel.query.filter(
                    TransactionsModel.AMOUNT.between(min_value, max_value)
                )
                .order_by(TransactionsModel.TIMESTAMP, TransactionsModel.AMOUNT)
                .all()
            ]
            if not transaction:
                raise LookupError(
                    f"No transactions were found for the value range {min_value} to {max_value}"
                )
            return {"Transaction": transaction}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")
