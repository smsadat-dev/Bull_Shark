from django.db import models 
from django.db.models import CharField, DateTimeField, ForeignKey, IntegerField

from .inventory import InventoryModel

class TransactionModel(models.Model):

    TRANSACTION_TYPE = (
        ("IN", "Stock In"),
        ("OUT", "Stock Out"),
        ("ADJUST", "Adjustment"),
    )

    inventory = ForeignKey(InventoryModel, on_delete=models.CASCADE)
    transaction_type = CharField(max_length=10, choices=TRANSACTION_TYPE)
    quantity = IntegerField()
    reference = CharField(max_length=255, blank=True)

    created_at = DateTimeField(auto_now_add=True)
