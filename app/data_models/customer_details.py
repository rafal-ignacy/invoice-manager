from dataclasses import dataclass


@dataclass
class CustomerDetails:
    email: str
    username: str
    full_name: str
    address_line1: str
    address_line2: str | None
    city: str
    post_code: str
    state_or_province: str | None
    country_code: str
