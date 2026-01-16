from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("A", "Admin"),
        ("S", "Staff"),
        ("V", "Viewer"),
    )

    role = models.CharField(
        max_length=1,
        choices=ROLE_CHOICES,
        default="V",
    )

    @property
    def role_display(self) -> str:
        return self.get_role_display() # type: ignore[attr-defined]

    def __str__(self):
        return f"{self.username} ({self.role_display})"