from dataclasses import dataclass
from typing import List

@dataclass
class LibraryDetail:
    id: int
    name: str
    is_deleted: bool
    created_at: str
    updated_at: str
    outlet_id: int
    guid: str | None
    uniq_id: str | None
    synchronized_at: str

@dataclass
class LibraryEntity:
    total_pages: int
    total_count: int