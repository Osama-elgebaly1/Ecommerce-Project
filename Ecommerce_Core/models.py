from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    Gender_Choices = [
        ('male','Male'),
        ('woman','Woman')
    ]
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    first_name = models.CharField( max_length=255,blank=True,null=True)
    last_name = models.CharField( max_length=255,blank=True,null=True)
    number = models.PositiveBigIntegerField(blank=True,null=True)
    address =  models.CharField(max_length=500,blank=True,null=True)
    city = models.CharField( max_length=50,blank=True,null=True)
    country = models.CharField( max_length=50,blank=True,null=True)
    zip_code =  models.IntegerField(blank=True,null=True)
    gender = models.CharField( max_length=50,choices=Gender_Choices,blank=True,null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    saved_cart = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} {self.first_name} {self.last_name}"


 
def create_profile(sender, instance, created, **kwargs):
    """
    Creating profile once new account is created .
    
    """
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile,User)




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



            