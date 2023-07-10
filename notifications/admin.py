from django.contrib import admin
from .models import Notifications
# Register your models here.
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('message', 'customer', 'time', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('message', 'customer')
    
admin.site.register(Notifications,NotificationsAdmin)
