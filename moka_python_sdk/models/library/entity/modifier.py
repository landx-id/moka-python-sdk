from dataclasses import dataclass
from typing import List

from .library import LibraryEntity, LibraryDetail

@dataclass
class ActiveOptions(LibraryDetail):
    modifier_id: int
    price: int
    position: int
    cogs: int

@dataclass
class ActiveItemModifier:
    id: int
    item_id: int
    modifier_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    synchronized_at: str
    
@dataclass
class ModifierDetail(LibraryDetail):
    business_id: int
    min_no_of_options: int
    max_no_of_options: int
    active_options: List[ActiveOptions]
    active_item_modifiers: List[ActiveItemModifier]

@dataclass
class ModifierEntity(LibraryEntity):
    modifier: List[ModifierDetail]
