from typing import Any

from django.contrib import admin
from django.http import HttpRequest

from invmngr.models import UserAuthProxyModel

@admin.register(UserAuthProxyModel)
class UserAuthAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False