from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.inventory import InventoryItem
from domain.entities.product import Product

class InventoryRepository(ABC):

    @abstractmethod
    def get_by_store_id(self, store_id: int,barcode:str) -> Optional[InventoryItem]:
        pass
    @abstractmethod
    def save_item(self, item: InventoryItem) -> Optional[InventoryItem]:
        pass
    @abstractmethod
    def get_low_stock_items(self, store_id: int) -> List[InventoryItem]:
        pass
    @abstractmethod
    def update_stock(self, inventory_id: int, new_stock: int) -> bool:
        pass