from django.urls import path

from api.views.task import TaskDetailView, TaskListCreateView

urlpatterns = [
    path("task/", TaskListCreateView.as_view(), name="task-list-create"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
