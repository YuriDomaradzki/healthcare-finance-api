import os

from flask import Flask
from flask_smorest import Api

from db import db
import models

from resources.patient import blp as PatientsBlueprint
from resources.phamacy import blp as PharmaciesBlueprint
from resources.transactions import blp as TransactionsBlueprint

ABSOLUTE_PATH = os.path.dirname(__file__)

def create_app():

    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "REST API for a healthcare company"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(ABSOLUTE_PATH, 'database/HealthCareFinance.db')}")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    api.register_blueprint(PatientsBlueprint)
    api.register_blueprint(PharmaciesBlueprint)
    api.register_blueprint(TransactionsBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)