from dataclasses import dataclass

@dataclass
class OrderStatusAttributes:
    """
    0: INCOMING
    1: ACCEPTED
    2: COMPLETED
    3: CANCELLED
    4: EXPIRED
    5: REJECTED
    6: DELIVERED
    """
    status_code: int

@dataclass
class OrderStatusData:
    attributes: OrderStatusAttributes

@dataclass
class OrderStatusEntity:
    data: OrderStatusData