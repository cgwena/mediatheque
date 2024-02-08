from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    nombreEmprunts = models.IntegerField(default=0)
