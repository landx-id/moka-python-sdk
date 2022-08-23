from dataclasses import dataclass
from typing import List

from .library import LibraryEntity, LibraryDetail

@dataclass
class TaxDetail(LibraryDetail):
    amount: int
    business_id: int

@dataclass
class TaxEntity(LibraryEntity):
    tax: List[TaxDetail]