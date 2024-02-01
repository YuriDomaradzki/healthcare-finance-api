from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from healthcare_finance_api.models import PharmacyModel
from healthcare_finance_api.utils import string_validation


blp = Blueprint("Pharmacies", __name__, description="Operations on Pharmacies")


@blp.route("/pharmacies")
class PharmaciesList(MethodView):

    @jwt_required()
    def get(self):
        try:
            pharmacies = [
                pharmacy.as_dict()
                for pharmacy in PharmacyModel.query.order_by(PharmacyModel.UUID).all()
            ]
            if not pharmacies:
                raise LookupError(f"No pharmacies")
            return {"Pharmacies": pharmacies}
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/pharmacy/name/<string:name>")
class PharmacyByName(MethodView):

    @jwt_required()
    def get(self, name):
        if not string_validation(text=name):
            raise ValueError("The name entered for the query is in an invalid format!")

        try:
            pharmacy = [
                pharmacy.as_dict()
                for pharmacy in PharmacyModel.query.filter_by(NAME=name.upper()).all()
            ]
            if not pharmacy:
                raise LookupError(f"No pharmacies called {name}")
            return {"Pharmacy": pharmacy}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/pharmacy/city/<string:city>")
class PharmacyByCity(MethodView):

    @jwt_required()
    def get(self, city):
        if not string_validation(text=city):
            raise ValueError("The city entered for the query is in an invalid format!")

        try:
            pharmacy = [
                pharmacy.as_dict()
                for pharmacy in PharmacyModel.query.filter_by(CITY=city.upper()).all()
            ]
            if not pharmacy:
                raise LookupError(f"No pharmacies in {city}")
            return {"Pharmacy": pharmacy}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/pharmacy/city/<string:city>/name/<string:name>")
class PharmacyByCityAndName(MethodView):

    @jwt_required()
    def get(self, city, name):
        if not string_validation(text=city) or not string_validation(text=name):
            raise ValueError(
                "The city or pharmacy name entered for the query is in an invalid format!"
            )

        try:
            pharmacy = [
                pharmacy.as_dict()
                for pharmacy in PharmacyModel.query.filter_by(
                    CITY=city.upper(), NAME=name.upper()
                ).all()
            ]
            if not pharmacy:
                raise LookupError(f"No pharmacies called {name} in {city}")
            return {"Pharmacy": pharmacy}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")
