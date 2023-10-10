from django import forms
from catalog.models import Colors

# количество для заказа
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    colors = forms.ModelChoiceField(label='Цвет', queryset=Colors.objects.all(), to_field_name="colors_product",
                                    empty_label="Выберите цвет")