from django.contrib import admin

from core.admin import UserTimestampMixinAdmin

from .models import Make, Model, Vehicle
from .forms import VehicleForm


class ModelInline(admin.TabularInline):
    model = Model
    extra = 0
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by', )


@admin.register(Make)
class MakeAdmin(UserTimestampMixinAdmin):
    inlines = [ModelInline]


@admin.register(Model)
class ModelAdmin(UserTimestampMixinAdmin):
    list_display = ('make', 'name', 'vehicle_type')
    list_filter = ('make', 'vehicle_type')
    search_fields = ('make', 'name',)


@admin.register(Vehicle)
class VehicleAdmin(UserTimestampMixinAdmin):
    form = VehicleForm
    list_display = ('vin', 'make', 'model', 'year', 'color',)
    list_filter = ('make', 'model', 'year', 'color',)
    search_fields = ('vin', 'make', 'model', 'year', 'color',)
    ordering = ('vin', 'make', 'model', 'year', 'color',)
    readonly_fields = ('created_by', 'updated_by')
    raw_id_fields = ('created_by', 'updated_by')
    date_hierarchy = 'created_at'
