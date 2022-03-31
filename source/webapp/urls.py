from django.contrib import admin
from django.urls import path

from webapp.views.product import ProductListView, ProductDetailView, ProductCreate, ProductUpdate, ProductDelete
from webapp.views.basket import add_product, CartView, remove_product
from webapp.views.order import OrderCreateView, UserOrdersView

app_name = "webapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ProductListView.as_view(), name="index"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="views"),
    path("product/create/", ProductCreate.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdate.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDelete.as_view(), name="product_delete"),
    path("<int:pk>/add/", add_product, name="add_product_cart"),
    path("cart/", CartView.as_view(), name="carts"),
    path("<int:pk>/remove/", remove_product, name="remove_product_cart"),
    path("order/create/", OrderCreateView.as_view(), name="order_create"),
    path("user/orders/", UserOrdersView.as_view(), name='user_orders'),
    path("gallery/", ProductListView.as_view())

]
