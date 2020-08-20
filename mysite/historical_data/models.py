from django.db import models

# Create your models here.

# This is the basic model to keep track of Bitcoin prices.
class PriceHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.PositiveIntegerField()
