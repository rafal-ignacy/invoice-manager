from dataclasses import dataclass
from typing import Dict
import json

from app.settings import ROOT_DIR


@dataclass
class DatabaseOperations:
    def get_queries_data(self) -> Dict:
        with open(ROOT_DIR + "/app/database/db_queries.json") as queries_file:
            queries_data = json.loads(queries_file.read())
        return queries_data
