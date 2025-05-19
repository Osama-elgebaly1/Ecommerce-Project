from django.db import models
from django.contrib.auth.models import User
from Ecommerce_Core.models import Product

# Create your models here.

class Order(models.Model):
    methods_choices = [
        ('card', 'Credit/Debit Card'),
        ('Cash on Delivery', 'Cash on Delivery')
    ]
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    full_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    payment_method = models.CharField(max_length=200,choices=methods_choices)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_shipped = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Order #{self.id} by {self.full_name}"




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    


