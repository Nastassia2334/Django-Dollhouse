from django.shortcuts import render
from catalog.models import Category
from .models import *


# Create your views here.
def delivery(request):
    category = Category.objects.all()
    delivery_goods = Delivery.objects.all()
    payment_goods = Payment.objects.all()
    context = {
        "delivery_goods": delivery_goods,
        "payment_goods": payment_goods,
        'all_category': category
    }
    return render(request, 'delivery.html', context)
