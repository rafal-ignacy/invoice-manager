from typing import Dict
import json


class RequestComponent:
    def get_file_data_dict(self, path: str) -> Dict:
        with open(path, "r") as file:
            file_data_dict = json.loads(file.read())
        return file_data_dict
