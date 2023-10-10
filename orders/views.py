from django.shortcuts import render
from .models import OrderProduct
from .forms import OrderCreateForm
from cart.cart import Cart
from catalog.models import Category


# Create your views here.
def order_create(request):
    category = Category.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderProduct.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])
                cart.save()
            # очистка корзины
            cart.clear()
            return render(request, 'created.html',
                          {'order': order, 'all_category': category})
    else:
        form = OrderCreateForm
    return render(request, 'create.html',
                  {'cart': cart, 'form': form, 'all_category': category})
