from django.db import models
from django.db.models import CharField, EmailField, TextField

# DB model for Supplier profile 
class SupplierModel(models.Model):
    
    name = CharField(max_length=255, blank=False, null=False)
    email = EmailField(max_length=255, blank=False, null=False)
    phone = CharField(max_length=15, blank=False, null=False)
    address = TextField(blank=False)

    def __str__(self):
        return self.name