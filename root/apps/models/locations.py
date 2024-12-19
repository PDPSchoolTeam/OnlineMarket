from django.db import models

class Coordinate(models.Model):
    x = models.CharField(max_length=300)
    y = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.x}, {self.y}"

    class Meta:
        verbose_name = "Delivery Address"
        verbose_name_plural = "Delivery Addresses"