"""
URL configuration for kaustik_order project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("orders/", include("orders.urls")),
    path("manager/", include("manager_panel.urls")),
    path("", include("main.urls")),
]
