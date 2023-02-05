from dataclasses import dataclass


@dataclass
class ItemDetails:
    item_ebay_id: str
    sku: str | None
    quantity: int
    price: str | float
