from dataclasses import dataclass

@dataclass
class OrderStatusEntity:
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