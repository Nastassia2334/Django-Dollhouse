from django.contrib import admin
from .models import Product, Category, Gallery, Colors


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery)
admin.site.register(Colors)
