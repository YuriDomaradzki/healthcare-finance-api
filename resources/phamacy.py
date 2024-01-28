from flask.views import MethodView
from flask_smorest import Blueprint, abort

from models import PharmacyModel


blp = Blueprint("Pharmacies", __name__, description="Operations on Pharmacies")


@blp.route("/pharmacies")
class Pharmacies(MethodView):

    def get(self):
        try:
            return {"Pharmacies": [pharmacy.as_dict() for pharmacy in PharmacyModel.query.order_by(PharmacyModel.UUID).all()]}
        except:
            abort(404, message="Error listing Pharmacies")