from dataclasses import dataclass
from typing import List

@dataclass
class InvoiceData:
    id: int
    status: str
    payment_no: str
    payment_type: str
    amount_pay: int
    amount_change: int
    total_discount_amount: float
    total_gratuity_amount: int
    total_item_price_amount: int
    total_tax_amount: int
    total_checkouts_amount: int
    is_refunded: bool
    refunded_reason: str
    refunded_date: str
    business_id: int
    customer_id: int | None
    discount_id: int | None
    is_deleted: bool
    created_at: str
    updated_at: str
    total_custom_price_amount: int
    include_gratuity_tax: bool
    parent_payment_id: int | None
    refund_amount: int
    refund_type: str
    card_no: str | None
    created_by: int
    note: str | None
    total_collected_amount: int
    server_id: int | None
    server_name: str | None
    server_title: str | None
    auth_code: str | None
    cc_name: str | None
    card_type: str | None
    transaction_number: str | None
    transaction_reference: str | None
    outlet_id: int
    guid: str | None
    synchronized_at: str
    uniq_id: str | None
    transaction_certificate: str | None
    transaction_status_info: str | None
    merchant_id: int | None
    mpos_device_id: int | None
    pg_mid: str | None
    pg_setting: str | None
    order_info: str | None
    tvr: str | None
    cvm_result: str | None
    aid: str | None
    transaction_date: str | None
    pii: str | None
    collected_by: str | None
    shift_id: int | None
    invoice_no: str | None
    invoice_deposit_amount: int | None
    invoice_due_date: str | None
    invoice_status: str | None
    latitude: float | None
    longitude: float | None
    refund_ids: list | str | None
    total_gross_sales: int
    total_net_sales: int
    is_refund_breakdown: bool
    customer_name: str | None
    customer_email: str | None
    customer_phone: str | None
    subtotal: int | None
    creator_name: str | None
    table_name: str | None
    collector_id: int | None
    cashlezz_transaction_id: str | None
    sms_id: str | None
    receipt_count: int | None
    order_id: str | None
    is_loyalty: bool | None
    total_redeem_amount: int | None
    is_offline: bool | None
    is_sales_type: bool
    uuid: str
    parent_payment_uuid: str


@dataclass
class InvoiceEntity:
    next_url: str
    completed: bool
    invoice: List[InvoiceData]
