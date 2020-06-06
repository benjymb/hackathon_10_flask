import os
from orator import DatabaseManager, Model
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Conexion:
    def __init__(self):
        self.default = os.getenv('ORM_DEFAULT')
        self.driver = os.getenv('ORM_DRIVER')
        self.host = os.getenv('DB_HOST')
        self.database = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.port = os.getenv('DB_PORT')

    def initialize(self):
        config = {
            'default': self.default,
            self.default: {
                'driver': self.driver,
                'host': self.host,
                'database': self.database,
                'user': self.user,
                'password': self.password,
                'port': self.port,
                'prefix': ''
            }
        }

        try:
            db = DatabaseManager(config)
            return db
        except Exception as e:
            print(str(e))

    def model(self):
        conn = self.initialize()
        Model.set_connection_resolver(conn)
        return Model
