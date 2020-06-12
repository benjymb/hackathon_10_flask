from orator import Model
from bcrypt import checkpw


class User(Model):

    __table__ = "users"
    __primary_key__ = "id"
    __timestamps__ = False
    __connection__ = "postgres"

    __guarded__ = ["id"]

    __fillable__ = ["username", "password", "rol", "name"]

    __casts__ = {
        "username": "str",
        "password": "str",
        "rol": "str",
        "name": "str"
    }

    __hidden__ = []

    def password_valid(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))



