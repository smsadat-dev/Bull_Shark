from django.db import models
from django.db.models import CharField, DateTimeField, DecimalField, ForeignKey, TextField

from bullshark.invmngr.models.category import CategoryModel

# DB model for Product 
class ProductModel(models.Model):

    name = CharField(max_length=255)
    description = TextField(blank=True)
    sku = CharField(max_length=255, null=False, unique=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)
    unit_price = DecimalField(max_digits=10, decimal_places=2)

    # Time records
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"