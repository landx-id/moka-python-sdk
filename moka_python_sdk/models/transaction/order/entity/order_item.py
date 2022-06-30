from dataclasses import dataclass
from typing import List

@dataclass
class ItemModifier:
    item_modifier_id: int
    item_modifier_name: str
    item_modifier_option_id: int
    item_modifier_option_name: str
    item_modifier_option_price: int

@dataclass
class OrderItemEntity:
    item_id: int
    item_name: str
    quantity: int
    item_variant_id: int
    item_variant_name: str
    note: str
    item_price_library: int
    category_id: int
    category_name: str
    item_discount_id: int
    item_discount_type: str
    item_discount_amount: int
    item_discount_guid: str
    item_discount_name: str
    item_modifiers: List[ItemModifier]
