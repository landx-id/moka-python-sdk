from dataclasses import dataclass
from typing import List
from .library import LibraryEntity, LibraryDetail

@dataclass
class GratuitiesDetail(LibraryDetail):
    business_id: int
    amount: int
    
@dataclass
class GratuitiesEntity(LibraryEntity):
    gratuities: List[GratuitiesDetail]