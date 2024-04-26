from sqlalchemy import func

from flask import request

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from healthcare_finance_api.models import PatientModel
from healthcare_finance_api.utils import string_validation


blp = Blueprint("Patients", __name__, description="Operations on patients")


@blp.route("/patients")
class PatientsList(MethodView):

    @jwt_required()
    def get(self):
        try:
            patients = [
                patients.as_dict()
                for patients in PatientModel.query.order_by(PatientModel.UUID).all()
            ]
            if not patients:
                raise LookupError(f"No Patients")
            return {"Patients": patients}
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/patient")
class Patient(MethodView):

    @jwt_required()
    def get(self):

        birthday = request.args.get("birthday")
        name = request.args.get("name")
        last_name = request.args.get("last_name")

        try:
            if birthday:
                if not all(char.isalnum() or char in ["/", "-"] for char in birthday):
                    raise ValueError(
                        "The birthday entered for the query is in an invalid format!"
                    )
                patients = [
                    patient.as_dict()
                    for patient in PatientModel.query.filter(
                        func.date(PatientModel.DATE_OF_BIRTH) == birthday
                    ).all()
                ]
            elif name:
                # Verifies if the search parameters received name value.
                # If so, verifies if is a valid string. Else, raises ValueError.
                if not string_validation(text=name):
                    raise ValueError(
                        "The first name entered for the query is in an invalid format!"
                    )

                patients = [
                        patients.as_dict()
                        for patients in PatientModel.query.filter_by(
                            FIRST_NAME=name.upper()
                        ).all()
                    ]
                # Verifies if the search parameters received last_name value.
                # If so, verifies if is a valid string. Else, raises ValueError.
                if last_name:
                    if not string_validation(text=last_name):
                        raise ValueError(
                            "The last name entered for the query is in an invalid format!"
                        )
                    patients = [
                        patients.as_dict()
                        for patients in PatientModel.query.filter_by(
                            FIRST_NAME=name.upper(), LAST_NAME=last_name.upper()
                        ).all()
                    ]
            else:
                raise ValueError(
                    "The query parameters entered isn't available!"
                    )

            if not patients:
                raise LookupError(f"No patients found for the search!")
            return {"Patient": patients}
        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")

