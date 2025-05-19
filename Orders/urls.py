from django.urls import path
from . import views


urlpatterns = [
    path('checkout/',views.Checkout,name='checkout'),
    path('orders_dash/',views.orders_dash,name='orders_dash'),
    path('admin/orders/mark-shipped/', views.mark_shipped, name='mark_shipped'),
    path('admin/orders/mark-unshipped/', views.mark_unshipped, name='mark_unshipped'),

]
