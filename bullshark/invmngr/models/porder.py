from django.db import models
from django.db.models import AutoField, CharField, DateTimeField, DecimalField, ForeignKey, IntegerField

from models.suppliers import SupplierModel
from models.warehouse import WareHouseModel

# DB model for Purchase order and Purchase order item table

class PurchaseOrderModel(models.Model):

    order_id = AutoField(primary_key=True)
    supplier_id = ForeignKey(SupplierModel, on_delete=models.CASCADE)
    warehouse_id = ForeignKey(WareHouseModel, on_delete=models.CASCADE)
    order_date = DateTimeField(null=False, blank=False)
    status = CharField(max_length=50)
    total_amount = DecimalField()

    def __str__(self): 
        return f"{self.supplier_id} - {self.order_date}"
