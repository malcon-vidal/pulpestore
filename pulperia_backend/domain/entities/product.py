from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    id: Optional[int]
    barcode: Optional[str]
    name: str
    category: str
    image_url: Optional[str] = None