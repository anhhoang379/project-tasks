class TaskStatus:
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

    CHOICES = (
        (NOT_STARTED, "not started"),
        (IN_PROGRESS, "in progress"),
        (COMPLETED, "completed"),
    )
