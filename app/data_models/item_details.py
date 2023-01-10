from dataclasses import dataclass


@dataclass
class ItemDetails:
    sku: str
    quantity: int
    price: float
