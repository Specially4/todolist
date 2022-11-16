from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User


@admin.register(User)
class Person(UserAdmin):
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    search_help_text = 'Use email, first_name, last_name, username'


admin.site.register(User, Person)
