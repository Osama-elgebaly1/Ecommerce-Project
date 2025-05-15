from django.shortcuts import render,redirect
from .cart import Cart

from django.http import HttpResponse
# Create your views here.






def cart_summary(request):
    # get all products using get_products func 
    # find a way to pass the quantity 
    # pass the total 
    pass







def update_cart(request,pk):
    # get the id from the url 
    # the  the  quants form post , if can be integer 
    # operate the add_cart , pass pk and quants 
    pass



def delete_cart(request,pk):
    # Get the id by the url 
    # operate the delete function and pass the id 
    pass




def add_cart(request,pk):
    # Get the id during the url 
    # get the quantity using Post request , check if can be integer
    # operate the  add_cart function  , pass the id , quants 
    pass
    