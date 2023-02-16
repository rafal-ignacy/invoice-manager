from dataclasses import dataclass
from typing import Dict, List, Any
import json

from app.data_models.invoice.customer_details import CustomerDetails
from app.data_models.invoice.item_details import ItemDetails


@dataclass
class InvoicePayloadHandler:
    def replace_customer_details(self, payload: Dict, customer_details: CustomerDetails) -> Dict:
        customer_payload = json.dumps(payload)
        for key in customer_details.__dict__.keys():
            customer_payload = customer_payload.replace("{" + key + "}", customer_details.__dict__[key])
        return json.loads(customer_payload)

    def replace_items_details(self, payload: Dict, items_details: List[ItemDetails]) -> List[Any]:
        items_details_list = []
        for item_details in items_details:
            item_payload = json.dumps(payload)
            for key in item_details.__dict__.keys():
                if item_details.__dict__[key] is not None:
                    item_payload = item_payload.replace("{" + key + "}", item_details.__dict__[key])
                else:
                    item_payload = item_payload.replace("{" + key + "}", "-")
            items_details_list.append(json.loads(item_payload))
        return items_details_list
