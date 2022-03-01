from django.contrib import sessions
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from webapp.models import Product, Category

from webapp.forms import ProductForm


class ProductListView(ListView):
    template_name = "product/index.html"
    model = Product
    context_object_name = "product"
    paginate_by = 10
    paginate_orphans = 1


    # def get(self, request, *args, **kwargs):
    #     if request.session["KEY"]:
    #         key = request.session["KEY"]
    #         count = key[f"{Product.objects.filter(pk=1)}"]
    #         print(type(count))
    #         count += 1
    #         key[f"{Product.objects.filter(pk=1)}"] = f"{count}"
    #         request.session["KEY"][f"{Product.objects.filter(pk=3)}"] = 1
    #     else:
    #         request.session["KEY"] = {f"{Product.objects.filter(pk=1)}": 5}
    #     print(f"{request.session['KEY']=}")
    #     return super().get(request, *args, **kwargs)



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


class ProductCreate(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = "product/create.html"
    form_class = ProductForm
    permission_required = "webapp.add_product"

    def form_valid(self, form):
        form.save()
        return redirect("webapp:index")

    def form_invalid(self, form):
        context = {"form": form}
        render(self.request, self.template_name, context)


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/update.html"
    permission_required = "webapp.change_product"

    def get_success_url(self):
        return reverse("webapp:index")


class ProductDelete(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "product/delete.html"
    permission_required = "webapp.delete_product"

    def post(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:index")

# class AddSessionProduct(CreateView):
#     def post(self, request, *args, **kwargs):
#         product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
#
#         # if request.session["KEY"]:
#         #     key = request.session["KEY"]
#         #     if key[f"{product.pk}"]:
#         #         count = key[f"{product.pk}"]
#         #         count += 1
#         #         key[f"{product.pk}"] = f"{count}"
#         #     else:
#         #         request.session["KEY"][f"{product.pk}"] = 1
#         # else:
#         #     request.session["KEY"] = {f"{product.pk}": 1}
#         # print(f"{request.session['KEY']=}")
#         return super().post(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return redirect("webapp:index")
#
#
# class CartView(ListView):
#     template_name = "product/cart.html"
#     context_object_name = "prod"
#     model = Product
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.session["KEY"]:
#             context["product"] = self.request.session["KEY"]
#             print(context["product"])
#         return context