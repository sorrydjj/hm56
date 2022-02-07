from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from webapp.models import Basket, Product, Category

from webapp.forms import ProductForm


class ProductListView(ListView):
    template_name = "product/index.html"
    model = Product
    context_object_name = "product"
    paginate_by = 5
    paginate_orphans = 1

    def post(self, request, *args, **kwargs):
        print(kwargs)
        if kwargs['pk'] in Basket.products:
            return


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


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/update.html"

    def get_success_url(self):
        return reverse("index")


class ProductDelete(DeleteView):
    model = Product
    template_name = "product/delete.html"

    def post(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("index")

# class BasketAdd(TemplateView):
#     template_name = "basket/basket.html"
#
#     def post(self, request, *args, **kwargs):
#         prod = get_object_or_404(Product, pk=self.kwargs.get('pk'))
#
#         if Basket.objects.filter(products=prod):
#             bask = Basket.objects.get(products=prod)
#             bask.counts += 1
#             bask.save()
#             print(bask.products)
#         else:
#             Basket.objects.create(products=prod, counts=1)
#         return redirect("index")


