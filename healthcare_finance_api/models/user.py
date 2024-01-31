import uuid

from healthcare_finance_api.models.db import db


class UsersModel(db.Model):

    __tablename__ = "USERS"

    UUID = db.Column(db.String, primary_key=True)#, default=str(uuid.uuid4()))
    USERNAME = db.Column(db.String, nullable=False)
    PASSWORD = db.Column(db.String, nullable=False)


    def as_dict(self) -> dict:
        """
            Returns the object's attributes in a dictionary.

            Returns
            -------
                A dictionary containing the object's attributes, where the keys are the attribute names.
        """
        return {
            'ID': self.UUID,
            'USERNAME': self.USERNAME
        }


    @classmethod
    def generate_uuid(cls) -> str:
        """
            Generates a UUID for a new user based on the existing UUIDs in the database.

            Returns
            -------
                A new UUID in the format 'USERXXXX', where XXXX is a sequential number.
        """
        intial_uuid = 'USER0001'
        last_uuid = cls.query.order_by(cls.UUID.desc()).first()
        if not last_uuid:
            return intial_uuid
        last_uuid = int(last_uuid.as_dict()['ID'][4:]) + 1
        return f"{intial_uuid[:4]}{last_uuid:04}"


    @classmethod
    def verify_username(cls, username: str) -> bool:
        """
            Checks if a username already exists in the database.

            Parameters
            ----------
                username: str,
                    the username to be checked.

            Returns
            -------
                Returns True if the username already exists, otherwise returns False.
        """
        existing_user = cls.query.filter_by(USERNAME=username).first()
        if existing_user:
            return True
        return False

