from django.conf import settings
from decimal import Decimal
from catalog import models


class Cart:

    def __init__(self, request):
        # получаем текущую сессию
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # новая корзина в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False, colors=None):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                     'colors': str(colors)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        # сохранение изменений в корзине
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        # удаление продукта из корзины
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # получаем id всех продуктов
        products_ids = self.cart.keys()
        products = models.Product.objects.filter(id__in=products_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
