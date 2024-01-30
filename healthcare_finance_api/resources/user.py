from typing import Optional, List

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError

from healthcare_finance_api.models.db import db
from healthcare_finance_api.models.user import UsersModel

from healthcare_finance_api.utils import string_is_alphanumeric


blp = Blueprint("Users", __name__, "Operations on users")


@blp.route("/user")
class User(MethodView):

    REQUIRED_KEYS = ['username', 'password']


    def __get_json_data(self):
        try:
            return request.get_json()
        except BadRequest as bre:
            abort(400, message='JSON file cannot be empty, must have username and password!')


    def __validate_keys(self, data: dict, keys: Optional[List]=REQUIRED_KEYS):
        try:
            valid_keys = all(key.lower() in [k.lower() for k in data.keys()] for key in keys)
            if not valid_keys:
                raise BadRequest(f"You must provide the following keys: {', '.join(keys)}")
        except BadRequest as bre:
            abort(400,  message=str(bre))


    def post(self):
        data = self.__get_json_data()
        self.__validate_keys(data=data)

        try:
            username = data.get('username')
            password = data.get('password')

            if not string_is_alphanumeric(text=username):
                raise ValueError("The username entered for is in an invalid format!")

            if UsersModel.verify_username(username=username):
                raise ValueError(f"User with username '{username}' already exists.")

            user = UsersModel(UUID=UsersModel.generate_uuid(), USERNAME=username, PASSWORD=password)

            db.session.add(user)
            db.session.commit()
            db.session.close()

            return {'Success': f'User {username} added!'}

        except ValueError as ve:
            abort(400, message=str(ve))
        except IntegrityError:
            abort(400, message='An user with this credentials already exists')
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


    def put(self):

        data = self.__get_json_data()
        keys = data.keys()
        try:
            if not 'username' in keys:
                raise BadRequest("You must provide at least the username")
            username = data.get("username")

            new_username = data.get("new_username") if 'new_username' in keys else ''
            new_password = data.get("new_password") if 'new_password' in keys else ''

            user = UsersModel.query.filter_by(USERNAME=username).first()

            if new_username:
                user.USERNAME = new_username
                print(user.USERNAME)
            if new_password:
                user.PASSWORD = new_password

            db.session.commit()
            db.session.close()

            return {'Sucess': 'The user was updated with successfully'}

        except ValueError as ve:
            abort(400, message=str(ve))
        except IntegrityError:
            abort(400, message='An user with this credentials already exists')
        except Exception as e:
            abort(500, message=f"An error has occurred: {str(e)}")


    def delete(self):

        data = self.__get_json_data()
        keys = data.keys()
        try:
            if not 'username' in keys:
                raise BadRequest("You must provide at least the username")
            username = data.get("username")

            user = UsersModel.query.filter_by(USERNAME=username).first()

            db.session.delete(user)
            db.session.commit()
            db.session.close()

            return {'Sucess': 'The user was deleted with successfully'}

        except ValueError as ve:
            abort(400, message=str(ve))
        except IntegrityError:
            abort(400, message='An user with this credentials already exists')
        except Exception as e:
            abort(500, message=f"An error has occurred: Check if the username you want to delete is correct.")

