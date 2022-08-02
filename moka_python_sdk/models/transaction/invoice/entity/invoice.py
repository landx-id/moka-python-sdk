from dataclasses import dataclass
from typing import List

from moka_python_sdk.models.transaction.invoice import invoice

@dataclass
class InvoiceData:
    id: str
    status: str
    payment_no: str
    payment_type: str
    amount_pay: int
    amount_change: int
    total_discount_amount: int
    total_gratuity_amount: int
    total_item_price_amount: int
    total_tax_amount: int
    total_checkouts_amount: int
    is_refunded: bool
    refunded_reason: str
    refunded_date: str
    business_id: int
    customer_id: int
    discount_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    total_custom_price_amount: int
    include_gratuity_tax: bool
    parent_payment_id: str
    refund_amount: int
    refund_type: str
    card_no: str
    created_by: int
    note: str
    total_collected_amount: int
    server_id: int
    server_name: str
    server_title: str
    auth_code: str
    cc_name: str
    card_type: str
    transaction_number: str
    transaction_reference: str
    outlet_id: int
    guid: str
    synchronized_at: str
    uniq_id: str
    transaction_certificate: str
    transaction_status_info: str
    merchant_id: int
    mpos_device_id: int
    pg_mid: str
    pg_setting: str
    order_info: str
    tvr: str
    cvm_result: str
    aid: str
    transaction_date: str
    pii: str
    collected_by: str
    shift_id: int
    invoice_no: str
    invoice_deposit_amount: int
    invoice_due_date: str
    invoice_status: str
    latitude: float | None
    longitude: float | None
    refund_ids: list
    total_gross_sales: int
    total_net_sales: int
    is_refund_breakdown: bool
    customer_name: str
    customer_email: str
    customer_phone: str
    subtotal: int
    creator_name: str
    table_name: str
    collector_id: int
    cashlezz_transaction_id: str
    sms_id: str
    receipt_count: int
    order_id: str
    is_loyalty: bool
    total_redeem_amount: int
    is_offline: bool
    is_sales_type: bool
    server_created_at: str
    total_rounding_amount: int
    bill_id: str
    tax_type: str
    gratuity_type: str
    uuid: str
    parent_payment_uuid: str


@dataclass
class InvoiceEntity:
    next_url: str
    completed: bool
    invoice: List[InvoiceData]
