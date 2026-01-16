from django.db import models
from django.db.models import CharField, DateTimeField, DecimalField, PositiveIntegerField

from models.user import UserModel

# DB model for Warehouse 
class WareHouseModel(models.Model):

    name = CharField(max_length=255)

    manager = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "S"}
    )

    capacity = PositiveIntegerField(null=True, blank=True)

    # Location records
    street = CharField(max_length=255)
    city = CharField(max_length=100)
    state = CharField(max_length=100, blank=True)
    postal_code = CharField(max_length=20, blank=True)
    country = CharField(max_length=50, default='Bangladesh')

    # Useful later for Geo analysis w/GeoDjango
    latitude = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Time records
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.city}"

