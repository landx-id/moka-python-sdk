from dataclasses import dataclass
from typing import List

from .item import ItemEntity

@dataclass
class DiscountEntity:
    discount_id: int
    discount_type: str
    discount_name: str
    discount_percentage: int
    discount_cash: int
    discount_amount: float
    discount_guid: str | None
    created_at: str
    updated_at: str

@dataclass
class ModifierEntity:
    id: int
    checkout_id: int
    modifier_id: int
    modifier_option_id: int
    modifier_name: str
    modifier_option_name: str
    price: int
    created_at: str
    updated_at: str
    cogs: int | None
    outlet_id: int
    payment_id: int
    discount_amount: float
    gross_sales: int
    net_sales: float
    redeem_amount: int
    uuid: str
    checkout_uuid: str
    payment_uuid: str
    discounts: List[DiscountEntity]


@dataclass
class CheckoutEntity(ItemEntity):
    id: int
    custom_amount: int
    discount_amount: float
    tax_amount: int
    business_id: int
    payment_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    item_discount: int
    item_price: int
    item_price_discount: float
    gratuity_amount: float
    item_price_discount_gratuity: float
    total_price: float
    item_price_quantity: int
    sku: str
    cogs: str | None
    gross_sales: int
    outlet_id: int
    position: int
    net_sales: float
    track_stock: bool
    item_image: str
    parent_checkout_id: int | None
    is_recipe: bool
    redeem_amount: float
    sales_type_id: int
    sales_type_name: str
    is_program_item: bool
    uuid: str
    payment_uuid: str
    parent_checkout_uuid: str | None
    price: int
    refunded_quantity: int
    modifiers: List[ModifierEntity]
    discounts: List[DiscountEntity]

