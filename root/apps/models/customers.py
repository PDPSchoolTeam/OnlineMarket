from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Name")
    last_name = models.CharField(max_length=50, verbose_name="Surname")
    phone = models.CharField(max_length=30, verbose_name="Phone Number")
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"