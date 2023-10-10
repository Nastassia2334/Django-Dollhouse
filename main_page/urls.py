from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_random, name='main_page'),
    path('search/', views.search, name='search_result'),
]
