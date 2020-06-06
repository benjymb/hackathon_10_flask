from app.connection.database import Conexion

conn = Conexion()
Model = conn.model()

class CompaniesModel(Model):
    __table__ = "companies"
    __primary_key__ = "id"
    __timestamps__ = False
    __connection__ = "postgres"

    __guarded__ = ["id"]

    __fillable__ = ["name", "ruc", "status"]

    __casts__ = {
        "name": "str",
        "ruc": "int",
        "status": "bool"
    }

    __hidden__ = []
