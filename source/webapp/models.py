from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(models.Model):
    names = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.names}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="name")
    descriptions = models.TextField(max_length=2000, blank=True, null=True, verbose_name="description")
    category = models.ForeignKey("webapp.Category", on_delete=models.PROTECT, related_name="categorys")
    count = models.PositiveIntegerField(verbose_name="counts", default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price", null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    products = models.ManyToManyField('webapp.Product', related_name='orders', verbose_name='Товары',
                                      through='webapp.OrderProduct', through_fields=['order', 'product'])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order", blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE,
                                verbose_name='Товар', related_name='order_products')
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE,
                              verbose_name='Заказ', related_name='order_products')
    qty = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.product.name} - {self.order.name}'

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
