from django.db import models
from .products import Product
from .customers import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Product")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Client")
    quantity = models.IntegerField(default=1,verbose_name="Amount")
    price = models.IntegerField(verbose_name="Price")
    address = models.CharField (max_length=50, default='', blank=True, verbose_name="Address")
    phone = models.CharField (max_length=50, default='', blank=True, verbose_name="Phone Number")
    date = models.DateField (default=datetime.datetime.today, verbose_name="Order placed time")
    status = models.BooleanField (default=False,verbose_name="Order status")
    delivery = models.BooleanField(default=False, verbose_name="Delivery status")
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"