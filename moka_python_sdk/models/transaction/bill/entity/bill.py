from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ItemVariant:
    id: int
    name: str
    price: int
    track_stock: bool

@dataclass
class BillItem:
    id: int
    name: str
    category_id: int
    quantity: str
    sales_type: str
    synchronized_at: str
    active_modifiers: List
    item_variants: List[ItemVariant]

@dataclass
class BillDetail:
    id: int
    bill_name: str
    server_name: str | None
    updated_at: str
    bill_sub_total_amount: float
    bill_total_amount: float
    items: List[BillItem]

@dataclass
class Table:
    tableId: Optional[int]
    tableGroupId: Optional[int]
    tableName: Optional[str]
    tableGroupName: Optional[str]

@dataclass
class BillEntity:
    id: int
    guid: str | None
    name: str

    createdAt: Optional[str]
    updatedAt: Optional[str]
    synchronizedAt: Optional[str]

    status: str

    outletId: Optional[int]
    tableId: Optional[int]
    cancelledBy: Optional[str]
    cancelledAt: Optional[str]
    cancelledReason: Optional[str]
    serveBy: Optional[int]

    pax: int
    createdByDevice: Optional[str]
    updatedByDevice: Optional[str]
    cancelledByName: Optional[str]
    serveByName: Optional[str]
    tables: Optional[List[Table]]


@dataclass
class BillData:
    data: List[BillEntity]
