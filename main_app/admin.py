from django.contrib import admin
from .models import Coin, FormatMaterial, Imperfection

# Register your models here.
admin.site.register(Coin)
admin.site.register(FormatMaterial)
admin.site.register(Imperfection)