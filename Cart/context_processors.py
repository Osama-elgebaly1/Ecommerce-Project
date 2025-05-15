from .cart import Cart

def cart_context(request):
    """
    Make cart length available in all templates.
    """
    cart = Cart(request)
    return {
        'cart_total_items': len(cart),
    }