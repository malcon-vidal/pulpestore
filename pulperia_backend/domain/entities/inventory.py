from dataclasses import dataclass
from typing import Optional

@dataclass
class Inventory:
    id: Optional[int]
    store_id: int
    product_id: int
    stock: int
    cost_price: float
    sale_price: float


    def is_low_stock(self) -> bool:
        """regla de negocio: determina si el producto esta por agotarse"""
        return self.stock <= self.min_stock

    def calculate_potential_profit(self) -> float:
        """calcula la ganancia unitaria estimada"""
        return self.sale_price - self.cost_price