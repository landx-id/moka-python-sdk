from dataclasses import dataclass
import dataclasses
from typing import List, Optional

@dataclass
class BusinessDetail:
    id: int
    name: str
    address: str
    suite: str
    city: str
    province: str
    postal_code: str
    description: str | None
    email: str
    phone: str
    logo: str | None
    notify_per_deposit: str | None
    notify_per_trans: str | None
    user_id: int
    is_deleted: bool
    created_at: str
    updated_at: str
    business_type_id: int | None
    business_category_id: int
    website: str
    twitter: str
    facebook: str
    instagram: str
    notes: str | None
    latitude: float | None
    longitude: float | None
    synchronized_at: str
    outlet_slot: int
    is_trial: bool
    current_plan: int
    expired_at: str
    last_payment_date: str | None
    trial_end_at: str


@dataclass
class BusinessInfo:
    business: BusinessDetail

@dataclass
class BusinessSetting:
    enable_tax: bool
    enable_gratuity: bool
    include_gratuity_tax: bool
    enable_rounding: bool

@dataclass
class LoyaltyCustomer:
    point_balance: int
    join_date: str

@dataclass
class CustomerDetail:
    id: int
    email: str
    name: str
    phone: str
    address: str | None
    city: str | None
    state: str | None
    postal_code: str | None
    business_id: int
    birthday: str | None
    is_deleted: bool
    created_at: str
    updated_at: str
    synchronized_at: str
    loyalty: LoyaltyCustomer

@dataclass
class CustomerEntity:
    customers: List[CustomerDetail]

@dataclass
class EarningRule:
    id: int
    type: str
    point: int
    amount: int

@dataclass
class RewardItem:
    id: int
    type: str
    category_name: str
    item_name: str
    item_variant_names: List[str]

@dataclass
class Reward:
    id: int
    reward_type: str
    discount: int
    discount_type: str
    max_discount_amount: float
    min_purchase_amount: int
    created_at: str
    created_by: str
    updated_at: str
    updated_by: str
    deleted_at: str
    deleted_by: str
    synchronized_at: str
    reward_items: List[RewardItem]
    redeem_point: int
    is_deleted: bool


@dataclass
class LoyaltyEntity:
    id: int
    business_id: int
    new_member_point: int
    program_revision: int
    status: str
    inactive_since: str
    reset_since: str
    created_at: str
    created_by: str
    updated_at: str
    updated_by: str
    deleted_at: str
    deleted_by: str
    synchronized_at: str
    is_sent_validation_code: bool
    earning_rules: List[EarningRule]
    rewards: List[dict]
    is_deleted: bool

@dataclass
class OutletDetail:
    id: int
    business_id: int
    name: str
    address: str
    phone_number: str
    city: str
    province: str
    postal_code: str
    latitude: float | None
    longitude: float | None
    is_deleted: bool
    created_at: str
    updated_at: str
    synchronized_at: str
    importing: bool
    exporting: bool
    notes: str | None
    start_date: str
    end_date: str
    is_paying: bool


@dataclass
class OutletEntity:
    outlets: List[OutletDetail]
    total_count: Optional[int]

@dataclass
class UserInfo:
    id: int
    email: str
    first_name: str
    last_name: str
    full_name: str
    business_id: int
    business_name: str
    outlet_ids: List[int]
    outlet_names: List[str]

@dataclass
class UserQuota:
    application_id: str
    resource: str
    quota: int
    refresh_at: str
