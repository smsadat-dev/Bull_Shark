from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import ROLE_CHOICES

class User(AbstractUser):
    

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
    

class UserAuthProxyModel(User):

    class Meta: 
        proxy = True
        app_label = 'auth'  # the trick to move under auths
        verbose_name = 'User'
        verbose_name_plural = 'Users'
