from django.contrib import admin

# Register your models here.
# contents/admin.py
from .models import *

admin.site.register(Article)
admin.site.register(Comment)