from django.db import models
from django.db.models import CharField, DateTimeField, ForeignKey, PositiveIntegerField

from .product import ProductModel
from .warehouse import WareHouseModel

# DB model for Inventory 
class InventoryModel(models.Model):
    
    warehouse = ForeignKey(WareHouseModel, on_delete=models.CASCADE)
    product = ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = PositiveIntegerField()
    max_capacity = PositiveIntegerField()

    # Location in warehouse
    location = CharField(max_length=50)

    # Time records
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["warehouse", "product"],
                name="unique_product_per_warehouse"
            )
        ]

        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'
