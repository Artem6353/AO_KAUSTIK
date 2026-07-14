from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена, ₽")

    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_NEW = "новое"
    STATUS_CONFIRMED = "подтверждено"
    STATUS_REJECTED = "отклонено"
    STATUS_CHOICES = (
        (STATUS_NEW, "Новое"),
        (STATUS_CONFIRMED, "Подтверждено"),
        (STATUS_REJECTED, "Отклонено"),
    )

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
        verbose_name="Пользователь",
    )
    fio = models.CharField(max_length=255, verbose_name="ФИО подавшего")
    org_name = models.CharField(max_length=255, verbose_name="Организация")
    inn = models.CharField(max_length=20, verbose_name="ИНН/КПП")
    legal_address = models.CharField(max_length=500, verbose_name="Юридический адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронная почта")
    items = models.JSONField(default=list, verbose_name="Позиции заказа")
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Сумма")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ {self.id} — {self.org_name}"
