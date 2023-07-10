from django.contrib import admin
from .models import Shipment
# Register your models here.
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'orders', 'delivery_location', 'shipment_cost', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('customer', 'delivery_location')

admin.site.register(Shipment, ShipmentAdmin)