from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField

# DB model for User 
class UserModel(AbstractUser):

    ROLE_CHOICES = (
        ("A", "Admin"),
        ("S", "Staff"),
        ("V", "Viewer"),
    )

    role = CharField(max_length=1, choices=ROLE_CHOICES)