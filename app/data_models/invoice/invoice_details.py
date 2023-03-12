from dataclasses import dataclass
from typing import List

from app.data_models.invoice.customer_details import CustomerDetails
from app.data_models.invoice.item_details import ItemDetails


@dataclass
class InvoiceDetails:
    issue_date: str
    service_date: str
    currency: str
    paid_amount: str | None
    rate: float
    customer_details: CustomerDetails
    items_details: List[ItemDetails]
