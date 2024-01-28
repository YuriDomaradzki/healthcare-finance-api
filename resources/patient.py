from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db

from models import PatientModel


blp = Blueprint("Patients", __name__, description="Operations on patients")


@blp.route("/patients")
class Patients(MethodView):

    def get(self):
        try:
            return {"Patients" :[
                patient.as_dict() for patient in PatientModel.query.order_by(PatientModel.UUID).all()
            ]}
        except:
            abort(404, message="Error listing Patients")

