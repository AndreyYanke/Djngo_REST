from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModelSet(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True)

