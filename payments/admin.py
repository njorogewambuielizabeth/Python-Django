from django.contrib import admin
from .models import Payment
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'amount', 'order_total', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('customer', 'payment_method', 'delivery_location')
admin.site.register(Payment, PaymentAdmin)
