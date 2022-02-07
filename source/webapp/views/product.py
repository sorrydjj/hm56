from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.models import Basket, Product, Category

from webapp.forms import ProductForm


class ProductListView(ListView):
    template_name = "product/index.html"
    model = Product
    context_object_name = "product"
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cont = self.object_list.filter(count__gte=1)
        context['product'] = cont
        return context



class ProductDetailView(DetailView):
    template_name = "product/view.html"
    model = Product



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context['product'] = product
        return context


class ProductCreate(CreateView):
    model = Product
    template_name = "product/create.html"
    form_class = ProductForm

    def form_valid(self, form):
        form.save()
        return redirect("index")

    def form_invalid(self, form):
        context = {"form": form}
        render(self.request, self.template_name, context)