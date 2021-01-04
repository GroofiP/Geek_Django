from django import forms

from ordersapp.models import Order, OrderItem


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label="цена",required=False)
    class Meta:
        model = OrderItem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

