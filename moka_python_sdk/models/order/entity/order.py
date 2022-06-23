from dataclasses import dataclass

@dataclass
class OrderAttributes:
    id: int

@dataclass
class OrderData:
    attributes: OrderAttributes

@dataclass
class OrderEntity:
    data: OrderData