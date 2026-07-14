from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("products/", views.products_view, name="products"),
    path("contacts/", views.contacts_view, name="contacts"),
    path("history/", views.history_view, name="history"),
]
