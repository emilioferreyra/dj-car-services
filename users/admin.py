from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail.admin import AdminImageMixin

from .forms import RegistrationForm
from .models import User


@admin.register(User)
class UserAdmin(AdminImageMixin, BaseUserAdmin):
    add_form = RegistrationForm
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2',
                ),
            },
        ),
    )
    list_display = (
        'email',
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (
            None,
            {'fields': ('avatar', 'first_name', 'last_name', 'password')},
        ),
        (
            _('Contact info'),
            {
                'fields': (
                    'email',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_superuser',
                    'is_staff',

                )
            },
        ),
        (_('Groups'), {'fields': ('groups', 'user_permissions')}),
        (
            _('Important dates'),
            {'fields': ('last_login', 'date_joined', 'created_date', 'updated_date')},
        ),
    )
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined', 'created_date', 'updated_date')
    filter_horizontal = ('groups', 'user_permissions')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_active', )
