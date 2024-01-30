import os

from flask import Flask
from flask_smorest import Api

from healthcare_finance_api.models.db import db

from healthcare_finance_api.resources.patient import blp as PatientsBlueprint
from healthcare_finance_api.resources.phamacy import blp as PharmaciesBlueprint
from healthcare_finance_api.resources.transactions import blp as TransactionsBlueprint
from healthcare_finance_api.resources.user import blp as UsersBlueprint

ABSOLUTE_PATH = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(ABSOLUTE_PATH, 
                             'healthcare_finance_api/database/HealthCareFinance.db')

def create_app():

    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "REST API for a healthcare company"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", 
                                                      f"sqlite:///{DATABASE_PATH}")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    api.register_blueprint(PatientsBlueprint)
    api.register_blueprint(PharmaciesBlueprint)
    api.register_blueprint(TransactionsBlueprint)
    api.register_blueprint(UsersBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)