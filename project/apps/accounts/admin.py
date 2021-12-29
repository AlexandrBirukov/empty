from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext as _
from .models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


@admin.register(User)
class UserAdmin(UserAdmin):
    form = CustomUserChangeForm
    list_display = ('email', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'token',
        )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('token',)
    ordering = ('email',)
