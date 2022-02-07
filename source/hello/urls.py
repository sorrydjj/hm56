"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views.product import ProductListView, ProductDetailView, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ProductListView.as_view(), name="index"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="views"),
    path("product/create/", ProductCreate.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdate.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDelete.as_view(), name="product_delete")
]
