from dataclasses import dataclass
from typing import Dict, Optional
import requests


@dataclass
class WebRequest:
    url: str
    headers: Optional[Dict] = None
    payload: Optional[Dict] = None

    def response(self):
        if self.payload is not None:
            request = requests.post(self.url, headers=self.headers, data=self.payload, timeout=10)
        else:
            request = requests.get(self.url, headers=self.headers, timeout=10)

        if request.status_code == 200:
            if request.headers.get("Content-Type") == "application/json" or request.headers.get("Content-Type") == "application/json; charset=utf-8":
                return request.json()
            else:
                return request.content
        else:
            print(request.text)
            raise request.raise_for_status()
