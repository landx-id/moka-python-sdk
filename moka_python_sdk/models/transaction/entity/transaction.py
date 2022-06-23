from dataclasses import dataclass
from typing import List
from .payment import PaymentEntity

@dataclass
class TransactionEntity:
    next_url: str
    completed: bool
    payments: List[PaymentEntity]
