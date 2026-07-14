from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import OrderForm


def order_create_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "Для оформления заказа необходимо авторизоваться.")
        return redirect("accounts:login")

    products = Product.objects.all()
    if request.method == "POST":
        form = OrderForm(request.POST, user=request.user)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            selected_products = form.cleaned_data["product"]
            qty = form.cleaned_data["qty"]
            items = []
            total = 0
            for p in selected_products:
                items.append({"name": p.name, "qty": qty, "price": float(p.price)})
                total += p.price * qty
            order.items = items
            order.total = total
            order.status = "новое"
            order.save()
            messages.success(request, "Заказ оформлен. Статус: «новое».")
            return redirect("main:history")
    else:
        form = OrderForm(user=request.user)

    return render(request, "orders/order.html", {"form": form, "products": products})
