from django.db import models

import constants

from ..managers import TaskManager


class Task(models.Model):
    objects = TaskManager()

    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ManyToManyField(
        "Member", related_name="assigned_tasks", db_index=True, blank=True
    )
    status = models.SmallIntegerField(
        choices=constants.TaskStatus.CHOICES,
        default=constants.TaskStatus.NOT_STARTED,
    )

    def __str__(self):
        return self.title
