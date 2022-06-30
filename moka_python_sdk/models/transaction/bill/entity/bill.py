from dataclasses import dataclass
from typing import List

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
    server_name: str
    updated_at: str
    bill_sub_total_amount: float
    bill_total_amount: float
    items: List[BillItem]

@dataclass
class Table:
    tableId: int
    tableGroupId: int
    tableName: str
    tableGroupName: str

@dataclass
class BillEntity:
    id: int
    guid: str
    name: str
    createdAt: str
    updatedAt: str
    synchronizedAt: str
    status: str
    outletId: int
    tableId: int
    cancelledBy: str
    cancelledAt: str
    cancelledReason: str
    serveBy: int
    pax: int
    receiptNo: str
    billDetail: BillDetail
    createdByDevice: str
    updatedByDevice: str
    cancelledByName: str
    tableGroupId: int
    tableName: str
    tableGroupName: str
    serveByName: str
    tables: List[Table]