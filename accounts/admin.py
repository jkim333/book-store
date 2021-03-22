from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': (
            'email',
            'username',
            'password',
            'last_login'
        )}),
        ('Additional Info', {'fields': (
            ('first_name', 'last_name'),
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password1', 'password2')
        }),
    )
    list_display = ['email', 'username',]

