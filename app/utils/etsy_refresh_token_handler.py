from dataclasses import dataclass
import json

from app.settings import ROOT_DIR


@dataclass
class EtsyRefreshTokenHandler:
    def save_refresh_token(self, refresh_token: str):
        credentials_file_path: str = ROOT_DIR + "/app/data/credentials.json"
        with open(credentials_file_path, "r") as file:
            credentials_dict = json.loads(file.read())
        credentials_dict["etsy_refresh_token"] = refresh_token
        credentials_str = json.dumps(credentials_dict)
        with open(credentials_file_path, "w") as file:
            file.write(credentials_str)
