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


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_first_name', 'get_last_name', 'get_username', 'get_city', 'get_country', 'bio')
    search_fields = ('user__username', 'bio', 'user__first_name', 'user__last_name', 'user__city', 'user__country')

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_city(self, obj):
        return obj.user.city
    get_city.short_description = 'City'

    def get_country(self, obj):
        return obj.user.country
    get_country.short_description = 'Country'

    get_first_name.admin_order_field = 'user__first_name'
    get_last_name.admin_order_field = 'user__last_name'
    get_username.admin_order_field = 'user__username'
    get_city.admin_order_field = 'user__city'
    get_country.admin_order_field = 'user__country'

# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(SecurityQuestions)
admin.site.register(UserProfile, UserProfileAdmin)