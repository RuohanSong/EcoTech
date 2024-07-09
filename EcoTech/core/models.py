from django.db import models
from django.contrib.auth.models import User

# For Sign Up
class CustomUser(User):
  # You can add custom fields to the User model here if needed
  pass

# Alternatively, create a separate user model (recommended for extensibility)
class MyUser(models.Model):
   username = models.CharField(max_length=100, unique=True)
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=100)
   # Add other fields as needed



