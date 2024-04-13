from django.urls import path

from api.views import (
    AvatarChangeView,
    BulkTasksView,
    ChangePasswordView,
    DeleteTasksView,
    LoginView,
    TaskDetailView,
    TaskFilterView,
    TaskListCreateView,
    UserView,
    AssignTaskView,
)

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="tasks_list_create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks_detail"),
    path("tasks/bulk/", BulkTasksView.as_view(), name="bulk_tasks"),
    path("tasks/delete/", DeleteTasksView.as_view(), name="delete_tasks"),
    path("tasks-filter", TaskFilterView.as_view(), name="task_filter"),
    path("users/login/", LoginView.as_view(), name="user_login"),
    path("users/", UserView.as_view(), name="user"),
    path(
        "users/change-password/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
    path(
        "users/change-avatar/",
        AvatarChangeView.as_view(),
        name="change_avatar",
    ),
    path('tasks/assignTask/', AssignTaskView.as_view(), name='assign_task'),
]
