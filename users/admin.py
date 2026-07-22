from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Netset roles",
            {
                "fields": (
                    "is_job_seeker",
                    "is_business_owner",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Netset roles",
            {
                "fields": (
                    "is_job_seeker",
                    "is_business_owner",
                )
            },
        ),
    )