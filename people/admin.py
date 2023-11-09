from django.contrib import admin

from .models import Customer
from .models import Employee
from .models import Person


class CustomBaseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    list_display_links = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'person_type',)
    list_filter = ('person_type', 'created_at', 'updated_by',)
    search_fields = ('first_name', 'last_name', 'email', 'phone',)


@admin.register(Employee)
class EmployeeAdmin(CustomBaseAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(CustomBaseAdmin):
    pass


@admin.register(Person)
class PersonAdmin(CustomBaseAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'person_type')
    list_display_links = ('first_name', 'last_name', 'email', 'phone', 'person_type')
