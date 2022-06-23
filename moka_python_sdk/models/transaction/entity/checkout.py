from dataclasses import dataclass
from typing import List

@dataclass
class DiscountEntity:
    discount_id: int
    discount_type: str
    discount_name: str
    discount_percentage: int
    discount_cash: int
    discount_amount: float
    discount_guid: str
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
    cogs: int
    outlet_id: int
    payment_id: int
    discount_amount: int
    gross_sales: int
    net_sales: int
    redeem_amount: int
    uuid: str
    checkout_uuid: str
    payment_uuid: str
    discounts: List[DiscountEntity]


@dataclass
class CheckoutEntity:
    id: int
    custom_amount: int
    item_variant_id: int
    quantity: int
    discount_amount: int
    tax_amount: int
    business_id: int
    payment_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    item_id: int
    item_discount: int
    item_price_library: int
    item_price: int
    item_price_discount: int
    gratuity_amount: int
    item_price_discount_gratuity: int
    total_price: int
    item_price_quantity: int
    category_name: str
    category_id: int
    item_name: str
    item_variant_name: str
    sku: str
    note: str
    cogs: str
    gross_sales: int
    outlet_id: int
    position: int
    net_sales: int
    track_stock: bool
    item_image: str
    parent_checkout_id: int
    is_recipe: bool
    redeem_amount: int
    sales_type_id: int
    sales_type_name: str
    is_program_item: bool
    uuid: str
    payment_uuid: str
    parent_checkout_uuid: str
    price: int
    refunded_quantity: int
    modifiers: List[ModifierEntity]
    discounts: List[DiscountEntity]

