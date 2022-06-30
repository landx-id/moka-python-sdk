from dataclasses import dataclass
from typing import List
from library import LibraryEntity

@dataclass
class CategoryDetail:
    id: int
    name: str
    description: str
    business_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    outlet_id: int
    guid: str
    uniq_id: str
    synchronized_at: str

@dataclass
class CategoryEntity(LibraryEntity):
    category: CategoryDetail