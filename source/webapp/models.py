from django.db import models



class Category(models.Model):
    names = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.names}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="name")
    descriptions = models.TextField(max_length=2000, blank=True, null=True, verbose_name="description")
    category = models.ForeignKey("webapp.Category", on_delete=models.PROTECT, related_name="categorys")
    count = models.IntegerField(verbose_name="counts", default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price", null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Basket(models.Model):
    products = models.ForeignKey("webapp.Product",
                                on_delete=models.PROTECT,
                                related_name="products"
                                )
    counts = models.IntegerField(verbose_name="count", default=0)

    def __str__(self):
        return f"{self.products} | {self.counts}"


    class Meta:
        db_table = "basket"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"