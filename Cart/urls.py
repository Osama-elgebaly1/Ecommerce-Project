from django.urls import path
from . import views

urlpatterns = [
    path('cart_summary/' ,views.cart_summary,name='cart_summary'),
    path('add_cart/<int:pk>' ,views.add_cart,name='add_cart'),
    path('delete_cart/<int:pk>' ,views.delete_cart,name='delete_cart'),
    


]
