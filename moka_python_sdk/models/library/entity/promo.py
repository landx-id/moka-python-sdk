from dataclasses import dataclass
from typing import List

@dataclass
class PromoRequirement:
    requirement_quantity: int
    requirement_type: str
    requirement_item_name: str

@dataclass
class PromoReward:
    amount: int
    reward_type: str
    reward_item_name: str

@dataclass
class PromoConfiguration:
    promo_multiplication: bool
    promo_days: str

@dataclass
class PromoDetail:
    business_id: int
    outlet_id: int
    outlet_name: str
    promo_id: int
    promo_name: str
    promo_type: str
    promo_description: str | None
    promo_start_date: str
    promo_end_date: str
    promo_status: str
    promo_requirement: List[PromoRequirement]
    promo_reward: List[PromoReward]
    promo_configuration: PromoConfiguration

@dataclass
class PromoEntity:
    promos: List[PromoDetail]