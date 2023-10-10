from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.warranty_return, name='warranty_return')
]
