from django.contrib import admin
from.models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_Number', 'email', 'location')
admin.site.register(Customer, CustomerAdmin)