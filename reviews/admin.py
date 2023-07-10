from django.contrib import admin
from .models import Review
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'number_of_stars', 'date')
    list_filter = ('number_of_stars',)
    search_fields = ('customer', 'product')

admin.site.register(Review, ReviewAdmin)