from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'is_admin', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('is_admin', 'is_active', 'is_staff', 'date_joined')
    ordering = ('-date_joined',)
