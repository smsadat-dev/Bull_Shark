from django.db import models
from django.db.models import AutoField, CharField, DateTimeField, FloatField, ForeignKey, TextField

from models.cetegory import CategoryModel

# DB model for Product 
class ProductModel(models.Model):

    prod_id = AutoField(primary_key=True)
    name = CharField(max_length=255, null=False, blank=False)
    description = TextField(blank=True)
    sku = CharField(max_length=255, null=False, blank=False, unique=True)
    cat_id = ForeignKey(CategoryModel, on_delete=models.CASCADE)
    unit_price = FloatField()

    # Time records
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"