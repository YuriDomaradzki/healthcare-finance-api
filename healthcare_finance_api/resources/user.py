from typing import Optional, List

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)

from werkzeug.exceptions import BadRequest, Unauthorized
from sqlalchemy.exc import IntegrityError

from blocklist import BLOCKLIST
from healthcare_finance_api.models.db import db
from healthcare_finance_api.models.user import UsersModel
from healthcare_finance_api.utils import string_is_alphanumeric, string_validation


blp = Blueprint("Users", __name__, "Operations on users")


@blp.route("/user")
class User(MethodView):

    def __get_json_data(self) -> dict:
        """
        Gets the JSON data from the request.

        Returns
        --------
            JSON data from the request.
        """
        try:
            return request.get_json()
        except BadRequest as bre:
            abort(
                400,
                message="JSON file cannot be empty, must have username and password!",
            )

    @jwt_required()
    def get(self):

        username = request.args.get('username')

        if not string_validation(text=username):
            raise ValueError(
                "The username entered for the query is in an invalid format!"
            )

        try:
            user = [
                user.as_dict()
                for user in UsersModel.query.filter_by(USERNAME=username).all()
            ]
            if not user:
                raise LookupError(f"No user with username {username}")
            return {"User": user}

        except ValueError as ve:
            abort(400, message=str(ve))
        except LookupError as le:
            abort(404, message=str(le))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")

    @jwt_required()
    def put(self):

        username = request.args.get('username')

        data = self.__get_json_data()
        keys = data.keys()
        try:
            new_username = data.get("new_username") if "new_username" in keys else ""
            new_password = data.get("new_password") if "new_password" in keys else ""

            user = UsersModel.query.filter_by(USERNAME=username).first()

            if new_username:
                user.USERNAME = new_username
            if new_password:
                user.PASSWORD = pbkdf2_sha256.hash(new_password)

            db.session.commit()
            db.session.close()

            return {"Sucess": "The user was updated with successfully"}

        except ValueError as ve:
            abort(400, message=str(ve))
        except IntegrityError:
            abort(400, message="An user with this credentials already exists")
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")

    @jwt_required()
    def delete(self):

        username = request.args.get('username')

        try:
            user = UsersModel.query.filter_by(USERNAME=username).first()

            db.session.delete(user)
            db.session.commit()
            db.session.close()

            return {"Success": "The user was deleted successfully"}, 200

        except ValueError as ve:
            abort(400, message=str(ve))
        except IntegrityError:
            abort(400, message="An user with this credentials already exists")
        except Exception as e:
            abort(
                500,
                message=f"An error has occurred: Check if the username you want to delete is correct.",
            )


@blp.route("/register")
class UserRegister(MethodView):

    def __get_json_data(self) -> dict:
        """
        Gets the JSON data from the request.

        Returns
        --------
            JSON data from the request.
        """
        try:
            return request.get_json()
        except BadRequest as bre:
            abort(
                400,
                message="JSON file cannot be empty, must have username and password!",
            )

    def __validate_keys(
        self, data: dict, keys: Optional[List] = ["username", "password"]
    ) -> None:
        """
        Validates that the required keys are present in the data.

        Parameters
        ----------
            data: str,
                Data to be validated.
            keys: Optional[List],
                List of required keys. Default is ['username', 'password'].
        """
        try:
            valid_keys = all(
                key.lower() in [k.lower() for k in data.keys()] for key in keys
            )
            if not valid_keys:
                raise BadRequest(
                    f"You must provide the following keys: {', '.join(keys)}"
                )
        except BadRequest as bre:
            abort(400, message=str(bre))

    def post(self):
        data = self.__get_json_data()
        self.__validate_keys(data=data)

        try:
            username = data.get("username")
            password = data.get("password")

            if not string_is_alphanumeric(text=username):
                raise ValueError("The username entered for is in an invalid format!")

            if UsersModel.verify_username(username=username):
                raise ValueError(f"User with username '{username}' already exists.")

            user = UsersModel(
                UUID=UsersModel.generate_uuid(),
                USERNAME=username,
                PASSWORD=pbkdf2_sha256.hash(password),
            )

            db.session.add(user)
            db.session.commit()
            db.session.close()

            return {"Success": f"User {username} added!"}, 201

        except ValueError as ve:
            abort(400, message=str(ve))
        except IntegrityError:
            abort(409, message="An user with this credentials already exists")
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/login")
class UserLogin(MethodView):

    def __get_json_data(self) -> dict:
        """
        Gets the JSON data from the request.

        Returns
        --------
            JSON data from the request.
        """
        try:
            return request.get_json()
        except BadRequest as bre:
            abort(
                400,
                message="JSON file cannot be empty, must have username and password!",
            )

    def __validate_keys(
        self, data: dict, keys: Optional[List] = ["username", "password"]
    ) -> None:
        """
        Validates that the required keys are present in the data.

        Parameters
        ----------
            data: str,
                Data to be validated.
            keys: Optional[List],
                List of required keys. Default is ['username', 'password'].
        """
        try:
            valid_keys = all(
                key.lower() in [k.lower() for k in data.keys()] for key in keys
            )
            if not valid_keys:
                raise BadRequest(
                    f"You must provide the following keys: {', '.join(keys)}"
                )
        except BadRequest as bre:
            abort(400, message=str(bre))

    def post(self):
        data = self.__get_json_data()
        self.__validate_keys(data=data)

        try:
            username = data.get("username")
            password = data.get("password")

            if not string_is_alphanumeric(text=username):
                raise ValueError("The username entered for is in an invalid format!")

            user = UsersModel.query.filter_by(USERNAME=username).first()

            if user and pbkdf2_sha256.verify(password, user.PASSWORD):
                access_token = create_access_token(identity=user.UUID, fresh=True)
                refresh_token = create_refresh_token(identity=user.UUID)
                return {"access_token": access_token, "refresh_token": refresh_token}
            raise Unauthorized("Invalid credentials")

        except ValueError as ve:
            abort(400, message=str(ve))
        except Unauthorized as un:
            abort(401, message=str(un))
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


@blp.route("/refresh")
class UserLoginRefresh(MethodView):

    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}


@blp.route("/logout")
class UserLogout(MethodView):

    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out."}
