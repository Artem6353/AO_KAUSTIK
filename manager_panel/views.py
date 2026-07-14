from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from orders.models import Order, Product


@staff_member_required
def manager_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all()

    if request.method == "POST":
        if "add_product" in request.POST:
            name = request.POST.get("name", "").strip()
            quantity = request.POST.get("quantity", "0")
            price = request.POST.get("price", "0")
            if name:
                Product.objects.create(name=name, quantity=int(quantity), price=float(price))
                messages.success(request, "Товар добавлен.")
            else:
                messages.error(request, "Укажите наименование продукции.")
            return redirect("manager_panel:dashboard")

        if "build_report" in request.POST:
            request.session["report"] = True
            return redirect("manager_panel:dashboard")

        order_id = request.POST.get("order_id")
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                if "confirm" in request.POST:
                    order.status = "подтверждено"
                    order.save()
                    messages.success(request, "Статус: подтверждено.")
                elif "reject" in request.POST:
                    order.status = "отклонено"
                    order.save()
                    messages.error(request, "Статус: отклонено.")
            except Order.DoesNotExist:
                pass
            return redirect("manager_panel:dashboard")

    total_orders = orders.count()
    confirmed = orders.filter(status="подтверждено").count()
    rejected = orders.filter(status="отклонено").count()
    new_count = orders.filter(status="новое").count()
    total_sum = sum(o.total for o in orders)

    report = None
    if request.session.get("report"):
        lines = [
            "ОТЧЁТ по заказам АО «Каустик»",
            f"Дата формирования: {request.POST.get('report_date', '')}",
            "--------------------------------------------------",
            f"Всего заказов:        {total_orders}",
            f"Подтверждено:         {confirmed}",
            f"Отклонено:            {rejected}",
            f"В работе (новые):     {new_count}",
            f"Общая сумма заказов: {total_sum:,.2f} ₽".replace(",", " "),
            "--------------------------------------------------",
            "Продукция в номенклатуре:",
        ]
        for p in products:
            lines.append(f"  - {p.name}: {p.quantity} ед., {p.price:,.2f} ₽/ед.".replace(",", " "))
        report = "\n".join(lines)
        request.session.pop("report", None)

    context = {
        "orders": orders,
        "products": products,
        "total_orders": total_orders,
        "confirmed": confirmed,
        "rejected": rejected,
        "new_count": new_count,
        "total_sum": total_sum,
        "report": report,
    }
    return render(request, "manager_panel/manager.html", context)
