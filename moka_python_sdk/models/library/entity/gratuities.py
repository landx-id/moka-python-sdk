from dataclasses import dataclass
from typing import List
from library import LibraryEntity

@dataclass
class GratuitiesDetail:
    id: int
    name: str
    amount: int
    business_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    outlet_id: int
    guid: str
    uniq_id: str
    synchronized_at: str
    deleted_at: str
    
@dataclass
class GratuitiesEntity(LibraryEntity):
    gratuities: List[GratuitiesDetail]