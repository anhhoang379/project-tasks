from django.utils.translation import gettext_lazy as _


class TaskStatus:
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

    CHOICES = (
        (NOT_STARTED, _(NOT_STARTED)),
        (IN_PROGRESS, _(IN_PROGRESS)),
        (COMPLETED, _(COMPLETED)),
    )
