from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView

from webapp.forms import OrderForm
from webapp.models import Product, Order, OrderProduct, User


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("webapp:index")
    template_name = "order/create.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        order = self.object
        if self.request.user.pk:
            order.user = self.request.user
            order.save()

        products = []
        order_products = []
        cont = {}
        for k, v in self.request.session["Cart"].items():
            product = Product.objects.get(pk=k)
            cont[product] = v

        for key, value in cont.items():
            product = key
            qty = value
            product.count -= qty
            products.append(product)
            order_product = OrderProduct(product=product, qty=qty, order=order)
            order_products.append(order_product)

        OrderProduct.objects.bulk_create(order_products)
        Product.objects.bulk_update(products, ("count",))
        del self.request.session["Cart"]
        return response


class UserOrdersView(LoginRequiredMixin, ListView):
    template_name = "order/user_order.html"
    model = Order


    def get_context_data(self, **kwargs):
        ord = Order.objects.filter(user=self.request.user.pk)
        kwargs['user_object'] = ord
        cont = {}

        for key in ord:
            print(key)
            cont[key] = OrderProduct.objects.filter(order=key.pk)

        kwargs['user_object'] = cont
        return super().get_context_data(**kwargs)