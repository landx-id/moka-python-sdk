from dataclasses import dataclass

@dataclass
class SubscriptionAttributes:
    id: int
    application_id: int
    business_id: int
    callback_uri: str
    event_id: int

@dataclass
class SubscriptionData:
    attributes: SubscriptionAttributes

@dataclass
class SubscriptionEntity:
    data: SubscriptionData
