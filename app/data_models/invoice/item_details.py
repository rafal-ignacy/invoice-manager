from dataclasses import dataclass


@dataclass
class ItemDetails:
    name: str
    code: str | None
    quantity: str
    price: str
