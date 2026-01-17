from django.contrib import admin 
from django.utils.html import format_html
from invmngr.models import InviteModel

@admin.register(InviteModel)
class InviteAdmin(admin.ModelAdmin):
    change_form_template = 'admin/invite_change_form.html'

    