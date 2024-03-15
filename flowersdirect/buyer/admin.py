from django.contrib import admin
from .models import FlowerItem, Category, OrderModel


# Register your models here.
admin.site.register(FlowerItem)
admin.site.register(Category)
admin.site.register(OrderModel)