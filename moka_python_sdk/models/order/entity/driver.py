from dataclasses import dataclass

@dataclass
class DriverAttributes:
    id: int
    name: str
    license_plate: str
    phone_number: str

@dataclass
class DriverData:
    attributes: DriverAttributes

@dataclass
class DriverEntity:
    data: DriverData