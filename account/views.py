from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserRegistrationForm

from catalog.models import Category


# Create your views here.
def account(request):
    all_category = Category.objects.all()
    return render(request, 'account.html', {'all_category': all_category})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем новый пользовательский объект
            new_user = user_form.save(commit=False)
            # Установливаем выбранный пароль
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем объект пользователя
            new_user.save()
            return render(request, 'register_detail.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


