from django.contrib import admin

from webapp.models import Category, Basket, Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(Product)