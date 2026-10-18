from typing import List
from domain.entities.inventory import InventoryItem
from domain.repositories.inventory_repository import IInventoryRepository

class GetLowAlertsUseCode:
    def __init__(self, inventory_repo: IInventoryRepository):
        self.inventory_repo = inventory_repo

    def execute(self, store_id: int) -> List[IInventoryRepository]:
        items = self.inventory_repo.get_low_stock_items(store_id)

        #filtrar asegurando la regla de negocio del dominio
        return [item for item in items if item.is_low_stock()]