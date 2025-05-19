from django.contrib import admin
from .models import *
from Orders.models import Order , OrderItem
# Register your models here.

admin.site.register([Product,Category,Profile,OrderItem,Order])


