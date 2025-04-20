from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.db.models import Q




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
    
    return render(request,'pages/index.html',{'products':products})



def category(request,pk):
    """
    Display all products belonging to a specific category.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the category to filter products by.

    Returns:
        HttpResponse: Renders the index.html template with the filtered products.
    """
    products = Product.objects.filter(category = pk)
    context = {
        'products':products
    }
    return render(request,'pages/index.html',context)



def about(request):
    """
    dislay about page 
    
    """
    return render(request,'pages/about.html',{})



def single_product(request,pk):
    """
    Display a single product's details.

    Args:
        request (HttpRequest): The incoming HTTP request.
        pk (int): The primary key of the product to be displayed.

    Returns:
        HttpResponse: Rendered HTML page with the product's details.
    """
    product = Product.objects.get(id = pk)
    context = {
        'product':product
    }
    return render(request,'pages/single_product.html',context)



def home(request):
    """
    Display the homepage with a list of all products.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML page showing all products.
    """
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'pages/index.html',context)

