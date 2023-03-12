from dataclasses import dataclass


@dataclass
class ItemDetails:
    platform_item_id: str
    sku: str | None
    quantity: int
    price: str | float
