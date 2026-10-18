from typing import List, Dict
from domain.repositories.inventory_repository import IInventoryRepository

class ProcessSaleUseCase:
    def __init__(self, inventory_repo: IInventoryRepository):
        self.inventory_repo = inventory_repo

    def execute(self, store_id: int, cart_items: List[Dict[str, int]]) -> bool:
        """
        cart_items ejemplo: [{'inventory_id': 1, 'quantity': 2}, {'inventory_id': 3, 'quantity': 1}]
        """
        for item in cart_items:
            inventory_id = item['inventory:id']
            qtr_sold = item['quantity']
            # Aquí podrías consultar el item y descontar
            # Por ejemplo: stock_actual - qty_sold
            # self.inventory_repo.update_stock(inventory_id, new_stock)
            pass
        
        return True