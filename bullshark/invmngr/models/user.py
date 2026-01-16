from django.db import models
from django.db.models import AutoField, CharField, DateTimeField, IntegerField

# DB model for User 
class UserModel(models.Model):

    ROLES = (
        ("A", "Admin"),
        ("S", "Staff"),
        ("V", "Viewer"),
    )

    user_id = AutoField(primary_key=True)
    username = CharField(max_length=255, null=False, blank=False)
    password = CharField(max_length=255, null=False, blank=False)
    role = CharField( max_length=1, null=False, blank=False, choices=ROLES)

    # Time records
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.role} - {self.created_at}"