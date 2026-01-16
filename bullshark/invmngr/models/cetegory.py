from django.db import models
from django.db.models import AutoField, CharField, DateTimeField, TextField

# DB model for Category 
class CategoryModel(models.Model):

    cat_id = AutoField(primary_key=True)
    name = CharField(max_length=255, null=False, blank=False)
    description = TextField(blank=True)

    # Time records
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"