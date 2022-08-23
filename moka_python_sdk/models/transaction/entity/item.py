from dataclasses import dataclass

@dataclass
class ItemEntity:
    item_id: int
    item_name: str
    quantity: int
    item_variant_id: int
    item_variant_name: str
    note: str | None
    item_price_library: int
    category_id: int
    category_name: str