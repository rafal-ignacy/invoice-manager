from dataclasses import dataclass
from typing import Dict, Optional
import requests


@dataclass
class WebRequest:
    url: str
    headers: Dict
    payload: Optional[Dict] = None

    def response(self):
        if self.payload is not None:
            request = requests.post(self.url, self.headers, json=self.payload, timeout=10)
        else:
            request = requests.get(self.url, self.headers, timeout=10)

        if request.status_code == 200:
            return request.json()
        else:
            raise request.raise_for_status()
