from django.contrib import admin
from .models import Order, ProductsInOrder

# Register your models here.
admin.site.register(Order)
admin.site.register(ProductsInOrder)
