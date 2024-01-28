from flask.views import MethodView
from flask_smorest import Blueprint, abort

from models import PharmacyModel


blp = Blueprint("Pharmacies", __name__, description="Operations on Pharmacies")


# TODO: SANITIZAR A ENTRADA E A SAÍDA
@blp.route("/pharmacies")
class PharmaciesList(MethodView):

    def get(self):
        try:
            return {"Pharmacies": [pharmacy.as_dict() for pharmacy in PharmacyModel.query.order_by(PharmacyModel.UUID).all()]}
        except:
            abort(404, message="Error listing Pharmacies")


# TODO: SANITIZAR A ENTRADA E A SAÍDA
@blp.route("/pharmacies/<string:name>")
class PharmacyByName(MethodView):

    def get(self, name):
        try:
            pharmacy = PharmacyModel.query.filter_by(NAME=name).first()
            return {'Pharmacy': pharmacy.as_dict()}
        except:
            abort(404, message=f"No Pharmacy with the name {name}")


# TODO: SANITIZAR A ENTRADA E A SAÍDA
@blp.route("/pharmacies/<string:city>")
class PharmacyByCity(MethodView):

    def get(self, city):
        pass