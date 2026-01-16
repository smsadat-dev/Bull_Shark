from django.db import models
from django.db.models import AutoField, CharField, DateTimeField, DecimalField, ForeignKey, IntegerField

from .supplier import SupplierModel
from .warehouse import WareHouseModel

# DB model for Purchase order and Purchase order item table
class PurchaseOrderModel(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("RECEIVED", "Received"),
        ("CANCELLED", "Cancelled"),
    )

    supplier = ForeignKey(SupplierModel, on_delete=models.CASCADE)
    warehouse = ForeignKey(WareHouseModel, on_delete=models.CASCADE)
    order_date = DateTimeField()
    status = CharField(max_length=20, choices=STATUS_CHOICES)
    total_amount = DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f"{self.supplier}"
