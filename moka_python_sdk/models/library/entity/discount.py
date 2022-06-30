from dataclasses import dataclass
from typing import List
from library import LibraryEntity

@dataclass
class DiscountDetail:
    id: int
    name: str
    amount: int
    type: str
    business_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    outlet_id: int
    guid: str
    uniq_id: str
    synchronized_at: str
    amount_format: str

class DiscountEntity(LibraryEntity):
    discount: List[DiscountDetail]