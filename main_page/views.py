from django.shortcuts import render
from catalog.models import Product, Category
from cart.cart import Cart


# на главной странице рандомно выводим товары в карусель
def product_random(request):
    category = Category.objects.all()
    product = Product.objects.all()
    cart = Cart(request)
    random_products = Product.objects.order_by('?')[:4]
    random_products_two = Product.objects.order_by('?')[:4]
    random_products_three = Product.objects.order_by('?')[:4]
    context = {
        "random_products": random_products,
        "random_products_two": random_products_two,
        "random_products_three": random_products_three,
        'product': product,
        'cart': cart,
        'all_category': category
    }
    return render(request, "main_page.html", context)


# для поиска по сайту
def search(request):
    category = Category.objects.all()
    # впеременную сохраняем текст поиска
    search_query = request.GET.get('q', '')
    # если совпадение есть
    if search_query:
        # ищем совпадение в имени
        product_list = Product.objects.filter(name__iregex=search_query)
        return render(request, 'search_result.html', {'product_list': product_list,
                                                      'all_category': category})
    else:
        return render(request, 'search_result.html', {'all_category': category})
