from sqlalchemy import func

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from healthcare_finance_api.models import TransactionsModel, PharmacyModel, PatientModel
from healthcare_finance_api.utils import string_validation, string_date_validation


blp = Blueprint("Transactions", __name__, description="Operations on transactions")


@blp.route("/transactions")
class Transactions(MethodView):

    def get(self):
        try:
            transactions = [transaction.as_dict() for transaction in TransactionsModel.query.order_by(TransactionsModel.UUID).all()]
            if not transactions:
                raise LookupError(f"No Transactions")
            return {'Transactions': transactions}
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/pharmacy/<string:name>")
class TranscationsByPharmacyName(MethodView):

    def get(self, name: str):
        if not string_validation(text=name):
            raise ValueError("The pharmacy name entered for the query is in an invalid format!")

        try:
            transaction = [transaction.as_dict() for transaction in TransactionsModel.query.join(TransactionsModel.pharmacy)
                                                                                           .filter(PharmacyModel.NAME == name.upper()).all()]
            if not transaction:
                raise LookupError(f"No transactions were found for the pharmacy {name}")
            return {'Transaction': transaction}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/pharmacy/<string:name>/date/<string:date>")
class TranscationsByDate(MethodView):

    def get(self, name: str, date: str):
        if not string_date_validation(date=date) or not string_validation(text=name):
            raise ValueError("The pharmacy name entered for the query is in an invalid format!")

        try:
            transaction = [transaction.as_dict() for transaction in TransactionsModel.query.join(TransactionsModel.pharmacy)
                                                                                           .filter(PharmacyModel.NAME == name.upper(),
                                                                                                   func.date(TransactionsModel.TIMESTAMP) == date)
                                                                                                   .all()]
            if not transaction:
                raise LookupError(f"No transactions were found for the pharmacy {name}")
            return {'Transaction': transaction}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/patient/<string:first_name>/<string:last_name>")
class TransactionsByPatientFirstAndLastName(MethodView):

    def get(self, first_name: str, last_name: str):
        if not string_validation(text=first_name) or not string_validation(text=last_name):
            raise ValueError("The patient's first or last name entered for the query is in an invalid format!")

        try:
            transaction = [transaction.as_dict() for transaction in TransactionsModel.query.join(TransactionsModel.patient)
                                                                                           .filter(PatientModel.FIRST_NAME == first_name.upper(),
                                                                                                   PatientModel.LAST_NAME == last_name.upper())
                                                                                                   .all()]
            if not transaction:
                raise LookupError(f"No transactions were found for the patient {first_name} {last_name}")
            return {'Transaction': transaction}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/transactions/byPeriod/<string:first_date>/<string:end_date>")
class TransactionsByPeriod(MethodView):

    def get(self, first_date: str, end_date: str):
        pass


blp.route("/transactions/byValues/<string:min_value>/<string:max_value>")
class TransactionsByValues(MethodView):

    def get(self, min_value: str, max_value: str):
        pass

