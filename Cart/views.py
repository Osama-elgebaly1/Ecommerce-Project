from django.shortcuts import render,redirect
from .cart import Cart
from django.contrib import messages

from django.http import HttpResponse

# ---------------------------
# 🛒 CART VIEWS
# ---------------------------




def cart_summary(request):
    """
    View to display the cart summary page.

    Retrieves all products currently in the user's cart, along with their
    quantities and total price, and renders them to a summary template.
    """
    cart = Cart(request)
    products = cart.get_products()
    print(products)
    quants = cart.get_quants()

    data = []

    for product in products:
        product_id = str(product.id)
        quantity = quants.get(product_id, 0)
        data.append({
            'product': product,
            'quantity': quantity
        })

    total = cart.get_total()

    return render(request, 'cart/cart_summary.html', {
        'products': data,
        'total': total
    })





def add_cart(request, pk):
    """
    Add a product to the cart.

    If the product already exists, its quantity won't increase in this view
    (based on current add_cart method behavior). Takes quantity from POST data.
    """
    cart = Cart(request)
    product_id = pk

    try:
        product_qty = int(request.POST.get('quantity', 1))

    except (ValueError, TypeError):
        product_qty = 1

    cart.add_cart(product_id, product_qty)
    messages.success(request, 'Product is added to cart successfully.')
    return redirect('home')








def delete_cart(request, pk):
    """
    Remove a product from the cart.
    Deletes the item with the specified primary key from the user's cart.
    """
    cart = Cart(request)
    cart.delete_cart(pk)
    messages.success(request, 'Product is removed successfully.')
    return redirect('home')
