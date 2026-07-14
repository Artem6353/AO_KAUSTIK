from django import forms
from .models import Order, Product


class OrderForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.SelectMultiple(attrs={"size": 4}),
        label="Выбор продукции",
    )
    qty = forms.IntegerField(min_value=1, initial=1, label="Количество (ед.)")

    class Meta:
        model = Order
        fields = ["fio", "org_name", "inn", "legal_address", "phone", "email"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields["fio"].initial = user.get_full_name() or user.username
