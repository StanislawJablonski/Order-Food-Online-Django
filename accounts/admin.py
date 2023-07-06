from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, UserProfile


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)