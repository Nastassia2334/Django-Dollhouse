from django.shortcuts import render
from .models import Contacts
from catalog.models import Category


# Create your views here.
def contacts(request):
    category = Category.objects.all()
    all_contacts = Contacts.objects.all()
    context = {
        "all_contacts": all_contacts,
        'all_category': category
    }
    return render(request, 'contacts.html', context)
