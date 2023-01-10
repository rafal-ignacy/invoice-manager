from dataclasses import dataclass


@dataclass
class OrderDetails:
    order_ebay_id: str
    platform: str
    order_date: str
    payment_status: str
    payment_date: str | None
    currency: str
    total: float
    delivery_total: float
