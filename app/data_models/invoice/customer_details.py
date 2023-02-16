from dataclasses import dataclass


@dataclass
class CustomerDetails:
    email: str
    full_name: str
    address_street: str
    city: str
    post_code: str
    country_code: str
    tax_country_code: str
