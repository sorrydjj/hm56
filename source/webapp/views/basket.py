from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from webapp.models import Product


def add_product(request, pk):
    if request.method == "GET":
        return HttpResponseNotFound('<h1>Page not found 404</h1>')
    else:
        product = Product.objects.get(pk=pk)
        if "Cart" in request.session:
            key = request.session["Cart"]
            if f'{product.pk}' in request.session["Cart"].keys():
                if key[f"{product.pk}"] < product.count:
                    count = key[f"{product.pk}"]
                    count += 1
                    key[product.pk] = count
                    request.session["Cart"] = key
                    messages.add_message(request, messages.SUCCESS, 'Товар успешно добавлен в количсетве 1!')
                else:
                    messages.add_message(request, messages.ERROR, 'Превышен лимит!')
            else:
                key[product.pk] = 1
                request.session["Cart"] = key
                messages.add_message(request, messages.SUCCESS, 'Товар успешно добавлен в количсетве 1!')
        else:
            request.session["Cart"] = {product.pk: 1}
            messages.add_message(request, messages.SUCCESS, 'Товар успешно добавлен в количсетве 1!')
        return redirect("webapp:index")


def remove_product(request, pk):
    if request.method == "GET":
        return HttpResponseNotFound('<h1>Page not found 404</h1>')
    else:
        product = Product.objects.get(pk=pk)
        if "Cart" in request.session:
            key = request.session["Cart"]
            if f'{product.pk}' in request.session["Cart"].keys():
                if key[f"{product.pk}"] <= 1:
                    del key[f"{product.pk}"]
                    request.session["Cart"] = key
                    messages.add_message(request, messages.WARNING, 'Товар успешно Удален!')
                else:
                    count = key[f"{product.pk}"]
                    count -= 1
                    key[product.pk] = count
                    request.session["Cart"] = key
                    messages.add_message(request, messages.SUCCESS, 'Товар успешно удален в количсетве 1!')
                    return redirect("webapp:carts")
            return redirect("webapp:carts")
        return redirect("webapp:carts")


class CartView(View):
    def get(self, request, *args, **kwargs):
        sums = []
        cont = {}
        if "Cart" in request.session:
            for k, v in request.session["Cart"].items():
                product = Product.objects.get(pk=k)
                cont[product] = v
                sums.append(product.price * v)
        context = {}
        context['product'] = cont
        context['sum'] = sum(sums)
        return render(request, "product/cart.html", context)

