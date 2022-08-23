from dataclasses import dataclass
from typing import List
from ....transaction.entity.item import ItemEntity

@dataclass
class ItemModifier:
    item_modifier_id: int
    item_modifier_name: str
    item_modifier_option_id: int
    item_modifier_option_name: str
    item_modifier_option_price: int

@dataclass
class OrderItemEntity(ItemEntity):
    item_discount_id: int
    item_discount_type: str
    item_discount_amount: float
    item_discount_guid: str
    item_discount_name: str
    item_modifiers: List[ItemModifier]
