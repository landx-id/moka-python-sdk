from dataclasses import dataclass
from typing import List
from .library import LibraryEntity, LibraryDetail

@dataclass
class CategoryDetail(LibraryDetail):
    business_id: int
    description: str | None

@dataclass
class CategoryEntity(LibraryEntity):
    category: List[CategoryDetail]
