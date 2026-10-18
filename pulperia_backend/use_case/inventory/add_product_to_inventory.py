from domain.entities.inventory import InventoryItem
from domain.repositories.inventory_repository import IInventoryRepository

class AddProductToInventoryUseCase:
    def __init__(self, inventory_repo: IInventoryRepository):
        self.invetory_repo = inventory_repo

    def execute(
            self,
            store_id: int,
            product_id: int,
            stock: int,
            min_stock: int,
            cost_price: float,
            sale_price: float
    ) -> InventoryItem:

    #crear un objeto de la entidad pura 
     item = InventoryItem(
        id=None,
        store_id=store_id,
        product_id=product_id,
        stock=stock,
        min_stock=min_stock,
        cost_price=cost_price,
        sale_price=sale_price
    )

        #persistir a traves de ka ubterfaz dek repositorio
     return self.inventory_repo.save(item)