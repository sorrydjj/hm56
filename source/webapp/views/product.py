from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.models import Basket, Product, Category

class ProductListView(ListView):
    template_name = "product/index.html"
    model = Product
    context_object_name = "product"
    paginate_by = 5
    paginate_orphans = 1