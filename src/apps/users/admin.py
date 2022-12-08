from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Personal info"),
            {
                "fields": ("mobile_phone",)
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "created_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("mobile_phone", "password1", "password2", "is_staff"),
            },
        ),
    )
    ordering = ('mobile_phone',)
    readonly_fields = ("last_login", "created_at", )
    list_display = ("mobile_phone", )
    search_fields = ("mobile_phone", )
    list_filter = ("is_active", "is_superuser",)
