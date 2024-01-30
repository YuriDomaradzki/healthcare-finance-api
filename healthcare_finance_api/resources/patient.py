from sqlalchemy import func

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from healthcare_finance_api.models import PatientModel
from healthcare_finance_api.utils import string_validation


blp = Blueprint("Patients", __name__, description="Operations on patients")


@blp.route("/patients")
class PatientsList(MethodView):
    def get(self):
        try:
            patients = [patients.as_dict() for patients in PatientModel.query.order_by(PatientModel.UUID).all()]
            if not patients:
                raise LookupError(f"No Patients")
            return {'Patients': patients}
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/patient/name/<string:name>")
class PatientByFullName(MethodView):

    def get(self, name: str):
        if not string_validation(text=name):
            raise ValueError("The first name entered for the query is in an invalid format!")

        try:
            patients = [patients.as_dict() for patients in PatientModel.query.filter_by(FIRST_NAME=name.upper()).all()]
            if not patients:
                raise LookupError(f"No patient called {name}")
            return {'Patient': patients}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/patient/name/<string:name>/lastName/<string:last_name>")
class PatientByFullName(MethodView):

    def get(self, name: str, last_name: str):
        if not string_validation(text=name) or not string_validation(text=last_name):
            raise ValueError("The first or last name entered for the query is in an invalid format!")

        try:
            patients = [patients.as_dict() for patients in PatientModel.query.filter_by(FIRST_NAME=name.upper(), 
                                                                                        LAST_NAME=last_name.upper()).all()]
            if not patients:
                raise LookupError(f"No patient called {name} {last_name}")
            return {'Patient': patients}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/patient/birthday/<string:birthday>")
class PatientByBirthday(MethodView):

    def get(self, birthday: str):
        if not all(char.isalnum() or char in ['/', '-'] for char in birthday):
            raise ValueError("The birthday entered for the query is in an invalid format!")

        try:
            patient = [patient.as_dict() for patient in PatientModel.query.filter(func.date(PatientModel.DATE_OF_BIRTH) == birthday).all()]
            if not patient:
                raise LookupError(f"No patient borned in {birthday}")
            return {'Patient': patient}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")

