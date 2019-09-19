from django.db.models import DateTimeField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_at = DateTimeField(auto_now_add=True, null=True)
    custom_time = DateTimeField(default=None, null=True)
