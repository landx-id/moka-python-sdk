from dataclasses import dataclass
from .order_item import OrderItemEntity

@dataclass
class OrderEntity:
    customer_phone_number: str
    sales_type_id: int
    sales_type_name: str
    client_created_at: str
    application_order_id: str
    payment_type: str
    note: str | None
    complete_order_notification_url: str
    accept_order_notification_url: str
    cancel_order_notification_url: str
    assign_expedition_notification_url: str
    discount_id: int
    discount_type: str
    discount_amount: float
    discount_guid: str | None
    discount_name: str
    order_items: OrderItemEntity

@dataclass
class OrderId:
    id: int