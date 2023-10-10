from django.urls import path
from . import views


urlpatterns = [
    path('', views.category, name='catalog'),
    path('<slug:category_slug>/', views.product_category, name='product_category'),
    path('<slug:category_slug>/<str:product_slug>/', views.product, name='product_one')
]