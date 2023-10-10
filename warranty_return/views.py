from django.shortcuts import render
from .models import WarrantyReturn
from catalog.models import Category


# Create your views here.
def warranty_return(request):
    category = Category.objects.all()
    actions = WarrantyReturn.objects.all()
    context = {
        "actions": actions,
        'all_category': category
    }
    return render(request, 'warranty_return.html', context)
