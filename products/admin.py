from django.contrib import admin

# Register your models here.

from .models import Product


#Register Model Into Admin Site
admin.site.register(Product)