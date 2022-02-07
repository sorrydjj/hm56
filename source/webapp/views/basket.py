from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.models import Basket, Product, Category
from webapp.forms import BasketForm

class BasketAddProduct(CreateView):
    model = Basket
    form_class = BasketForm
    template_name = "basket/basket.html"

    def post(self, request, *args, **kwargs):
        prod = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        if Basket.objects.filter(products=prod):
            bask = Basket.objects.get(products=prod)
            bask.counts += 1
            bask.save()
        else:
            Basket.objects.create(products=prod, counts=1)
        return redirect("index")
