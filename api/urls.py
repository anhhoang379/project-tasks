from django.urls import path

from api.views import (
    BulkTasksView,
    DeleteTasksView,
    TaskDetailView,
    TaskListCreateView,
)

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="tasks-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
    path("tasks/bulk/", BulkTasksView.as_view(), name="bulk_tasks"),
    path("tasks/delete/", DeleteTasksView.as_view(), name="delete_tasks"),
]
