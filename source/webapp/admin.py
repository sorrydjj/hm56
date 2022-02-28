from django.contrib import admin

from webapp.models import Category, Product, Order, OrderProduct
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)