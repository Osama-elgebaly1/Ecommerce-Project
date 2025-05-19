from django.shortcuts import render,redirect
from .forms import CheckoutForm
from Cart.cart import Cart
from django.http import HttpResponse
from .models import Order,OrderItem
from Ecommerce_Core.models import Profile
from django.views.decorators.http import require_POST

# Create your views here.


@require_POST
def mark_shipped(request):
    order = Order.objects.get(id = request.POST['order_id'])
    order.is_shipped = True
    order.save()
    return redirect('orders_dash')

@require_POST
def mark_unshipped(request):
    order = Order.objects.get(id=request.POST['order_id'])
    order.is_shipped = False
    order.save()
    return redirect('orders_dash')


def orders_dash(request):
    if request.user.is_staff:


        shipped_orders = Order.objects.filter(is_shipped=True)
        Unshipped_orders = Order.objects.filter(is_shipped=False)
        return render(request,'order/orders_dash.html',{'shipped':shipped_orders,
                                                        'unshipped':Unshipped_orders})
    else:
        return redirect('home')


def Checkout(request):
    """
        Handles the checkout process:
        - Prefills the form with user profile data (if authenticated).
        - Validates submitted form.
        - Creates an Order and related OrderItem entries.
        - Clears the session cart after successful checkout.
        - Clears the user's saved cart (if logged in).
    """
    cart = Cart(request)
    total = cart.get_total()

    if request.user.is_authenticated:
        profile = request.user.profile

        initial_data = {
            'full_name': f'{profile.first_name} {profile.last_name}' if profile.first_name and profile.last_name else '',
            'address': profile.address,
            'city' : profile.city,
            'country' : profile.country,
            'phone' : profile.number,

        }

    else:
        initial_data = {}

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            full_name = request.POST['full_name']
            address = request.POST['address']
            city = request.POST['city']
            country = request.POST['country']
            phone = request.POST['phone']
            payment_method = request.POST['payment_method']

            # Creating order 
            order = Order.objects.create(
                full_name = full_name,
                address = f'Address :{address} \n City : {city} \n Country : {country} ',
                phone = phone ,
                payment_method = payment_method,
                total = total,
            )

            # creating order items 
            products = cart.get_products()
            products_data = []

            for product in products: 
                product_id = str(product.id)
                quantity = cart.get_quants().get(product_id, 0)
                products_data.append({
                    'product': product,
                    'quantity': quantity
                })


            for item in products_data:
                product = item['product']
                quantity = item['quantity']
                if product.on_sale:
                    price = product.price_after_discount
                else:
                    price = product.price

                order_item = OrderItem.objects.create(order=order,
                                                      product=product,
                                                      quantity=quantity,
                                                      price=price)
                
            
            # Deleting  the  cart from the session 
            # Deleting saved cart if authenticated 
            del request.session['cart']
            if request.user.is_authenticated:
                profile = Profile.objects.filter(user=request.user)
                profile.update(saved_cart='')

            
            return render(request,'order/order_success.html')
        
    else:
        form = CheckoutForm(initial=initial_data)
        return render(request,'order/checkout.html',{'form':form,
                                                       'total':total})
            


