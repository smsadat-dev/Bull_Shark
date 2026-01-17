from django.db import models
from django.db.models import CharField, DateTimeField, TextField

# DB model for Category 
class CategoryModel(models.Model):

    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True)

    # Time records
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'