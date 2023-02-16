from dataclasses import dataclass
from typing import Dict
import mysql.connector  # type: ignore
import json


from app.settings import ROOT_DIR
from app.utils.logger import Logger


@dataclass
class Database:
    def __init__(self, function_name: str):
        self.function_name: str = function_name
        self.logger = Logger()
        db_config = self.get_config()
        try:
            self.database = mysql.connector.connect(host=db_config["host"], database=db_config["database"],
                                                    user=db_config["user"], password=db_config["password"])
        except Exception:
            self.logger.error("Cannot connect to database")
        else:
            self.logger.info("Connected to database")
            self.cursor = self.database.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.logger.error(self.function_name)
        else:
            self.logger.info(self.function_name)
        self.database.close()
        self.logger.info("Closed database")

    def get_config(self) -> Dict:
        with open(ROOT_DIR + "/app/database/db_config.json") as db_config_file:
            db_config = json.loads(db_config_file.read())
        return db_config

    def commit(self):
        self.database.commit()
