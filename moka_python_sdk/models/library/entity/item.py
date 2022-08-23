from dataclasses import dataclass
from typing import List

from .library import LibraryEntity, LibraryDetail
from .category import CategoryDetail

@dataclass
class ImageDetail:
    url: str

@dataclass
class ItemVariant:
    id: int
    name: str
    sku: str
    price: int
    in_stock: int
    stock_alert: int
    position: int
    item_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    add_inventory: int
    track_stock: bool
    alert: bool
    cogs: int | None
    synchronized_at: str
    last_modified: str
    outlet_id: int
    guid: str | None
    uniq_id: str | None
    track_cogs: bool
    is_saved: bool
    sales_type_items: List[dict]

@dataclass
class ActiveModifier(LibraryDetail):
    business_id: int
    modifier_options: List[dict]

@dataclass
class ItemDetail(LibraryDetail):
    description: str | None
    image: ImageDetail
    business_id: int
    category_id: int
    is_recipe: bool
    is_sales_type_price: bool
    background_color: str
    alert: bool
    category: CategoryDetail
    item_variants: List[ItemVariant]
    active_modifiers: List[ActiveModifier]


@dataclass
class ItemEntity(LibraryEntity):
    items: List[ItemDetail]