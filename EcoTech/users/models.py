from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Member(User):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.username
