from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField

FORMATS = (
    ('C', 'Circle'),
    ('O', 'Octagon'),
    ('H', 'Hollow'),
)

MATERIALS = (
    ('G', 'Golden'),
    ('S', 'Silver'),
    ('B', 'Bronze'),
)

# Create your models here.
class Coin(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    value = MoneyField(max_digits=4, decimal_places=2, default_currency='USD')
    year = models.IntegerField('Year the coin was struck')
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.country
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coin_id': self.id})
    
class FormatMaterial(models.Model):
    format = models.CharField(
        max_length=1, 
        choices=FORMATS,
        default=FORMATS[0][0]
    )
    material = models.CharField(
        max_length=1,
        choices=MATERIALS,
        default=MATERIALS[0][0]
    )

    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_format_display()} on {self.get_material_display()}"