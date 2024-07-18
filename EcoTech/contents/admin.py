from django.contrib import admin

# Register your models here.
# contents/admin.py
from .models import Article

admin.site.register(Article)