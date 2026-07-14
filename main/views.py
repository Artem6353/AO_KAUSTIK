from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import Product, Order


def index_view(request):
    return render(request, "main/index.html")


def products_view(request):
    products = Product.objects.all()
    is_manager = request.user.is_authenticated and request.user.role == "manager"
    return render(request, "main/products.html", {"products": products, "is_manager": is_manager})


def contacts_view(request):
    return render(request, "main/contacts.html")


@login_required
def history_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "main/history.html", {"orders": orders})
