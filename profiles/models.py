from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    code = models.TextField(blank=True)
