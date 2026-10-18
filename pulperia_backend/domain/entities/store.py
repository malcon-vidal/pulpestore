from dataclasses import dataclass
from typing import Optional

@dataclass
class Store:
    id: Optional[int]
    owner_id: int
    name: str
    address: str
    latitude: float
    longitude: float