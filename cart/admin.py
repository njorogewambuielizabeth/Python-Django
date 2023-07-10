from django.contrib import admin
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'number_of_products', 'shipment_cost', 'payment_options')
    list_filter = ('payment_options',)
    search_fields = ('product',)

admin.site.register(Cart, CartAdmin)