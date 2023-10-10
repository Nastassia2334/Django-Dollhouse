from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderProduct


# Register your models here.
# Inline режим позволяет включить модель для отображения на той же странице редактирования,
# что и родительская модель
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    fields = ["first_name", "last_name", "email", "address",
              "postal_code", "city", "delivery_type", "payment_type"]
    inlines = [OrderProductInline]



admin.site.register(Order, OrderAdmin)
