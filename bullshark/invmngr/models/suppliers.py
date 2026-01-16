from django.db import models
from django.db.models import AutoField, CharField, EmailField, TextField

# DB model for Supplier profile 

class SupplierModel(models.Model):
    
    supplier_id = AutoField(primary_key=True)
    name = CharField(max_length=255, blank=False, null=False)
    enail = EmailField(max_length=255, blank=False, null=False)
    phone = CharField(max_length=15, blank=False, null=False)
    address = TextField(blank=False)
