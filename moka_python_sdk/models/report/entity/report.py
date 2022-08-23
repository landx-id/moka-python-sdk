from dataclasses import dataclass
from typing import List

@dataclass
class CategorySalesDetail:
    name: str
    items_sold: int
    gross_sales: float
    discount: float
    refund: float
    net_sales: float

@dataclass
class CategorySalesEntity:
    category_sales: List[CategorySalesDetail]
    total_items_sold: int
    total_gross_sales: float
    total_discounts: float
    total_refunds: float
    total_net_sales: float

@dataclass
class ReportDetail:
    name: str
    title: str
    number_of_transactions: int
    total: float

@dataclass
class CollectorSalesEntity:
    total_number_of_transactions: int
    grand_total: float
    reports: List[ReportDetail]

@dataclass
class ModifierOption:
    option_id: int
    option_name: str
    quantity: int
    gross_sales: float
    discount: float
    refund: float
    net_sales: float


@dataclass
class ModifierDetail:
    modifier_id: int
    modifier_name: str
    quantity: int
    gross_sales: float
    discount: float
    refund: float
    net_sales: float
    modifier_options: List[ModifierOption]


@dataclass
class ModifierSalesEntity:
    modifiers: List[dict]
    total_quantity: int
    total_gross_sales: float
    total_discounts: float
    total_refunds: float
    total_net_sales: float

@dataclass
class DiscountDetail:
    discount_id: int
    name: str
    amount: float
    discount_applied: float
    count: int
    discount_type: str
    refund: float
    net_discount: float

@dataclass
class DiscountSalesEntity:
    discounts: List[DiscountDetail]
    total_count: int
    total_discounts_applied: float
    total_refunds: float

@dataclass
class ReportTax:
    name: str
    amount: float
    taxable_amount: float
    tax_collected: float

@dataclass
class TaxSalesEntity:
    reports_taxes: List[ReportTax]
    total_tax_collected: float

@dataclass
class ReportGratuity:
    name: str
    amount: int
    gratuity_collected: float

@dataclass
class GratuitySalesEntity:
    reports_gratuities: List[ReportGratuity]
    total_gratuity_collected: float

@dataclass
class ServerDetail:
    server_id: int | None
    server_name: str | None
    server_title: str | None
    number_transaction: int
    collected: int

@dataclass
class ServerSalesEntity:
    servers: List[ServerDetail]
    total_collected: float
    total_number_of_transactions: int

@dataclass
class ItemSalesDetail:
    name: str
    sku: str
    category_name: str
    item_sold: int
    item_refunded: int
    gross_sales: float
    discount: float
    refund: float
    net_sales: float
    cogs: float
    redemption: float
    gross_profit: float


@dataclass
class ItemSalesEntity:
    item_sales: List[dict]
    total_item_sold: int
    total_gross_sales: float
    total_discounts: float
    total_net_sales: float
    total_refund: float

@dataclass
class SalesSummaryEntity:
    gross_sales: float
    discounts: float
    refunds: float
    net_sales: float
    gratuities: float
    taxes: float
    total_collected: float
    number_of_transactions: int
    rounding_amount: float
    redemption: float

@dataclass
class ReportObject:
    payment_type: str
    number_of_transactions: int
    collected: float

@dataclass
class ReportDetail:
    cash_or_card: List[ReportObject]
    invoice: List[ReportObject]
    other: List[ReportObject]

@dataclass
class PaymentMethodsEntity:
    total_number_of_transactions: int
    total_collected: float
    reports: ReportDetail
