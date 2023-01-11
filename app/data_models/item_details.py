from dataclasses import dataclass


@dataclass
class ItemDetails:
    item_ebay_id: str
    sku: str
    quantity: int
    price: str
