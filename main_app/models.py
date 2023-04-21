from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Coin(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    value = MoneyField(max_digits=4, decimal_places=2, default_currency='USD')
    year = models.IntegerField()
    description = models.TextField(max_length=300)