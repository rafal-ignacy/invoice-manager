from dataclasses import dataclass


@dataclass
class CustomerDetails:
    email: str | None
    username: str
    full_name: str
    address_line1: str
    address_line2: str | None
    city: str
    post_code: str | None
    state_or_province: str | None
    country_code: str
