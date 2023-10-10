from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog import models
from .cart import Cart
from .forms import CartAddProductForm
from catalog.models import Category


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    # id продукта с запроса
    product = get_object_or_404(models.Product, id=product_id)
    # иницмализация формы
    form = CartAddProductForm(request.POST)

    # проверка
    if form.is_valid():
        # получаем данные из формы
        cd = form.cleaned_data

        # добавляем в корзину
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],
                 colors=cd['colors'])

    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    # id продукта с запроса
    product = get_object_or_404(models.Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    category = Category.objects.all()
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart, 'all_category': category})
