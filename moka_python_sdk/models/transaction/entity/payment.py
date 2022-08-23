from dataclasses import dataclass
from typing import List

from ..invoice.entity.invoice import InvoiceData

from .checkout import CheckoutEntity

@dataclass
class PaymentTax:
    id: int
    name: str
    amount: int
    total: float
    taxable_amount: float
    payment_id: int
    created_at: str
    updated_at: str
    tax_id: int
    uuid: str
    payment_uuid: str

@dataclass
class PaymentGratuity:
    id: int
    name: str
    amount: float
    total: float
    payment_id: int
    created_at: str
    updated_at: str
    gratuity_id: int
    uuid: str
    payment_uuid: str

@dataclass
class PaymentDiscount:
    id: int
    payment_id: int
    discount_id: int
    discount_amount: float
    discount_name: str
    discount_type: str
    is_deleted: bool
    created_at: str
    updated_at: str
    discount_cash: int
    uuid: str
    payment_uuid: str


@dataclass
class PaymentEntity:
    id: str
    payment_no: str
    created_at: str
    updated_at: str
    parent_payment_created_at: str
    total_collected: int
    total_item_price_amount: int
    name: str
    parent_payment_id: int | None
    payment_type: str
    payment_type_label: str
    customer_id: str | None
    payment_note: str
    discounts: float
    subtotal: float
    gratuities: int
    taxes: int
    tendered: int
    change: int
    include_gratuity_tax: bool
    enable_tax: bool
    enable_gratuity: bool
    card_type: str | None
    card_no: str | None
    transaction_date: str
    transaction_time: str
    collected_by: str
    served_by: str
    synchronized_at: str
    outlet_id: int
    pg_mid: str | None
    mpos_device_id: str | None
    transaction_certificate: str | None
    transaction_status_info: str | None
    mpos_transaction_date: str | None
    merchant_id: str | None
    transaction_reference: str | None
    transaction_number: str | None
    order_info: str | None
    cc_name: str | None
    pii: str | None
    guid: str | None
    uniq_id: str | None
    invoice_due_date: str | None
    invoice_no: str | None
    invoice_deposit_amount: str | None
    invoice_payment_records: List[object]
    payment_taxes: List[PaymentTax]
    payment_gratuities: List[PaymentGratuity]
    payment_discounts: List[PaymentDiscount]
    payment_refunds: List[InvoiceData]
    checkouts: List[CheckoutEntity]