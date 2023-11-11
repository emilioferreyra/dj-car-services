from django.contrib import admin

from core.admin import UserTimestampMixinAdmin

from .models import Catalog


@admin.register(Catalog)
class CatalogAdmin(UserTimestampMixinAdmin):
    list_display = ('name', 'description', 'category', )
    list_filter = ('category', )
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by', )
