from django.contrib import admin

from ..models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "name",
        "dob",
        "hometown",
        "school",
    ]

    list_select_related = ["user"]
