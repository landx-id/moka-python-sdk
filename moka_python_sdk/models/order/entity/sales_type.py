from dataclasses import dataclass

@dataclass
class SalesTypeAttributes:
    id: int
    name: str
    
class SalesTypeData:
    attributes: SalesTypeAttributes

class SalesTypeEntity:
    data: SalesTypeData