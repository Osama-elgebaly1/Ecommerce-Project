from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponse



def search(request):
    """
       
    Handles the search functionality for products based on a search query. 
    
    This view retrieves a search query from the GET parameters, filters products 
    based on whether their name or description contains the search term (case-insensitive),
    and renders the results on the 'index.html' template.

    """
    search = request.GET.get('search')
    products = Product.objects.filter(
        Q(name__icontains=search) | Q(description__icontains=search))
    
    return render(request,'Ecommerce-core/index.html',{'products':products})



def category(request,pk):
    """
    Lists all products under a specific category.
    """
    products = Product.objects.filter(category = pk)
    context = {
        'products':products
    }
    return render(request,'Ecommerce-core/index.html',context)



def about(request):
    """
    dislay about page 
    
    """
    return render(request,'Ecommerce-core/about.html',{})



def single_product(request,pk):
    """
    Shows the details of a single product by its ID.
    """
    product = Product.objects.get(id = pk)
    context = {
        'product':product
    }
    return render(request,'Ecommerce-core/single_product.html',context)



def home(request):
    """
    Displays all products on the homepage with sale badges and categories.
    """
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'Ecommerce-core/index.html',context)

