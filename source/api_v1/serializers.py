from rest_framework import serializers

from webapp.models import Product, Category, OrderProduct, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("names",)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ("id", "name", "descriptions", "category", "count", "price")
        read_only_fields = ("id",)


class OrderProductSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'qty')
        read_only_fields = ('id', )


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ("name", "phone", "address", "created_at", "user", "order_products")
        read_only_fields = ("id", )

    def create(self, validated_data):
        products = []
        cart_products = []
        order_products = []
        order = Order.objects.create(name=validated_data["name"], phone=validated_data["phone"], address=validated_data["address"], user=validated_data["user"])

        for cart in validated_data["order_products"]:
            prod = OrderProduct()
            prod.order = order
            prod.product = cart["product"]
            prod.qty = cart["qty"]
            cart_products.append(prod)
            order_products.append(prod)

        for key in cart_products:
            product = Product.objects.get(pk=key.product.pk)
            product.count -= key.qty
            products.append(product)

        OrderProduct.objects.bulk_create(order_products)
        Product.objects.bulk_update(products, ("count",))
        return order