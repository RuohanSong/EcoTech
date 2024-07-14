from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class MemberAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('city', 'country')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('city', 'country')}),
    )


# Register your models here.
admin.site.register(Member, MemberAdmin)
