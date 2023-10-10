from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm

from cart.cart import Cart


# Create your views here.
def category(request):
    all_category = Category.objects.all()
    context = {
        'all_category': all_category,
    }
    return render(request, "catalog.html", context)


def product_category(request, category_slug):
    all_category = Category.objects.all()
    category = get_object_or_404(Category, category_slug=category_slug)
    all_products = Product.objects.filter(category=category)
    context = {
        "category": category,
        "all_products": all_products,
        'all_category': all_category
    }
    return render(request, "product_category.html", context)


def product(request, category_slug, product_slug):
    all_category = Category.objects.all()
    category = Category.objects.get(category_slug=category_slug)
    products = Product.objects.get(product_slug=product_slug)
    images = Gallery.objects.filter(product__id=products.id)
    form = CartAddProductForm()
    cart = Cart(request)
    random_products = Product.objects.order_by('?')[:4]
    context = {
        "product": products,
        'cart_product_form': form,
        'images': images,
        'all_category': all_category,
        "random_products": random_products,
        'cart': cart,
    }

    return render(request, "product.html", context)


def product_cart(request, product_id):
    products = get_object_or_404(Product, id=product_id)

    cart_product_form = CartAddProductForm()
    return render(request, 'cart.html', {'product': products,
                                         'cart_product_form': cart_product_form})