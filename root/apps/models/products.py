from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name="Name")
    price = models.IntegerField(default=0, verbose_name="Price")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name="Category")
    description = models.CharField(max_length=250, default='', blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to='uploads/products/', verbose_name="Photo")

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"