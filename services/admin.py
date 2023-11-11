from django.contrib import admin

from core.admin import UserTimestampMixinAdmin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    min_num = 1
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by',)


@admin.register(Order)
class OrderAdmin(UserTimestampMixinAdmin):
    list_display = ('id', 'vehicle', 'status', 'total')
    list_filter = ('status',)
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by',)
    inlines = (OrderItemInline,)
