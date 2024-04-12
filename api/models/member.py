from django.contrib.auth.models import User
from django.db import models

from ..managers import MemberManager


class Member(models.Model):
    objects = MemberManager()

    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)

    name = models.CharField(max_length=255, db_index=True)
    dob = models.DateField()
    hometown = models.CharField(max_length=255)
    school = models.CharField(max_length=255)

    def __str__(self):
        return "{} ({})".format(self.name, self.user.username)
