from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float

@dataclass
class Order:
    id: Optional[int]
    store_id: int
    client_id: Optional[int]
    order_type: str  # e.g., 'online', 'in-store'
    items: list[OrderItem]
    total: float
    status: str  # e.g., 'pending', 'completed', 'canceled'

    def mark_as_ready(self):
        """reglas de negocio para cambiar el estado del encargo"""
        if self.order_type == 'online' and self.status == 'in-store':
            self.status = 'listo'