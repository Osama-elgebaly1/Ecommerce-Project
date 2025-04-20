from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        



class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    image = models.ImageField( upload_to='media/products/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    price_after_discount = models.DecimalField(max_digits=10,decimal_places=2,null= True,blank=True)
    on_sale = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.on_sale:
            self.price_after_discount = None

        super().save(*args,**kwargs)



            