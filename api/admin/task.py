from django.contrib import admin

from ..models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "assigned_to",
        "status",
    ]

    list_select_related = ["assigned_to"]
