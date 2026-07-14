from django.urls import path
from . import views

app_name = "manager_panel"

urlpatterns = [
    path("", views.manager_dashboard, name="dashboard"),
]
