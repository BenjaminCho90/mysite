from django.contrib import admin

from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['customer_name']

admin.site.register(Customer,CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name']

admin.site.register(Product, ProductAdmin)

admin.site.register(Order)
# Register your models here.
