from django.db import models

# Create your models here.
class Cart(models.Model):
    price = models.IntegerField()
    number_of_products = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1) 
    product = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cart/') 
    shipment_cost = models.IntegerField()
    payment_options = models.CharField(max_length=255)

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Cart #{self.pk} - {self.product}"
    

    def add_product(self,product):
        self.product.add(product)
        self.save()
        return self
    
    def get_total(self):
        products = self.product
        total = 0
        for prod in products:
            total += prod.price
            return total