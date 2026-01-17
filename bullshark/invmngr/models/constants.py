from django.db import models

ROLE_CHOICES = (
    ('A', 'Admin'),
    ('S', 'Staff'),
    ('V', 'Viewer'),
)

class InviteStatus(models.TextChoices):
    PENDING = 'P', 'Pending'
    ACCEPTED = 'A', 'Accepted'
    EXPIRED = 'E', 'Expired'
    REVOKED = 'R', 'Revoked'