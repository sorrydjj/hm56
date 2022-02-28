from django.contrib import admin
from django.urls import path

from webapp.views.product import ProductListView, ProductDetailView, ProductCreate, ProductUpdate, ProductDelete

app_name = "webapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ProductListView.as_view(), name="index"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="views"),
    path("product/create/", ProductCreate.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdate.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDelete.as_view(), name="product_delete"),

]
