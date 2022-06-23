from dataclasses import dataclass

@dataclass
class AutoAcceptAttributes:
    auto_accept_status: bool

@dataclass
class AutoAcceptData:
    attributes: AutoAcceptAttributes

@dataclass
class AutoAcceptEntity:
    data: AutoAcceptData