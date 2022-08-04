from dataclasses import dataclass
from typing import List
from .library import LibraryEntity, LibraryDetail

@dataclass
class DiscountDetail(LibraryDetail):
    business_id: int
    amount: int
    type: str
    amount_format: str

class DiscountEntity(LibraryEntity):
    discount: List[DiscountDetail]