from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "price")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "org_name", "fio", "status", "total", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("org_name", "fio", "inn")
    readonly_fields = ("created_at",)
