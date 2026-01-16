from django.db import models
from django.db.models import AutoField, CharField, DateTimeField, ForeignKey, PositiveIntegerField

from models.product import ProductModel
from models.warehouse import WareHouseModel

# DB model for Inventory 
class InventoryModel(models.Model):
    inv_id = AutoField(primary_key=True)
    warehouse_id = ForeignKey(WareHouseModel, on_delete=models.CASCADE)
    prod_id = ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = PositiveIntegerField()
    max_capacity = PositiveIntegerField()

    # Location in warehouse
    location = CharField(max_length=50)

    # Time records
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

