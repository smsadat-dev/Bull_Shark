import uuid

from django.conf import settings
from django.db import models
from django.db.models import CharField, DateTimeField, DecimalField, EmailField, ForeignKey, ManyToManyField, UUIDField

from .constants import InviteStatus, ROLE_CHOICES
from .user import User
from .warehouse import WareHouseModel

class InviteModel(models.Model):

    email = EmailField(unique=True)
    role = CharField(max_length=1, choices=ROLE_CHOICES)
    warehouses = ManyToManyField(WareHouseModel, blank=True, related_name="invites")
    token = UUIDField(default=uuid.uuid4, unique=True)
    status = models.CharField(max_length=1, choices=InviteStatus.choices, default=InviteStatus.PENDING)
    invited_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="sent_invites")

    # Time records
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    accepted_at = models.DateTimeField(null=True, blank=True)

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                condition=models.Q(status=InviteStatus.PENDING),
                name="unique_pending_invite_per_email",
            )
        ]

        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["token"]),
            models.Index(fields=["status"]),
        ]

        ordering = ["-created_at"]

        verbose_name = 'Invite'
        verbose_name_plural = 'Invites'

    def __str__(self):
        return f"{self.email} ({self.get_status_display()})" # type: ignore
