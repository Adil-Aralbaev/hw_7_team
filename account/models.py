from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_chat_id = models.CharField(max_length=120)
    password = models.CharField(max_length=20,unique=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# class StaffUser(AbstractUser):
#     telegram_chat_id = models.CharField(max_length=120)
#     password = models.CharField(max_length=20)
#     is_staff = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.username
