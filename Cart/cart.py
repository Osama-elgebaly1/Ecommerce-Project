import json
from Ecommerce_Core.models import Product, Profile

class Cart:
    """
    A shopping cart system that uses Django sessions to store cart data.
    Also synchronizes with the user's profile if authenticated.
    """

    SESSION_KEY = 'cart'

    def __init__(self, request):
        """
        Initialize the cart using the session.
        If no cart exists, an empty one is created.
        """
        self.session = request.session
        self.request = request
        cart = self.session.get(self.SESSION_KEY)

        if not cart:
            cart = self.session[self.SESSION_KEY] = {}

        self.cart = cart

    def add_cart(self, pk, quantity=1):
        """
        Add a product to the cart.

        Args:
            pk (int): Product primary key.
            quantity (int): Quantity of product to add (default is 1).
        """
        product_id = str(pk)

        self.cart[product_id] = quantity

        self.session.modified = True
        self._update_user_cart()




    def delete_cart(self, pk):
        """
        Remove a product from the cart.

        Args:
            pk (int): Product primary key.
        """
        product_id = str(pk)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
            self._update_user_cart()

    def get_quants(self):
        """
        Get the raw cart dictionary (product_id → quantity).

        Returns:
            dict: Current cart contents.
        """
        return self.cart

    def __len__(self):
        """
        Return the total number of items in the cart.
        """
        return len(self.cart)

    def get_products(self):
        """
        Fetch product instances for all products in the cart.

        Returns:
            QuerySet: Django queryset of Product objects.
        """
        product_ids = [int(key) for key in self.cart.keys()]
        products = Product.objects.filter(id__in = product_ids)

        return products
    

    def get_total(self):
        """
        Calculate the total cost of all items in the cart,
        accounting for discounted prices when applicable.

        Returns:
            float: Total cost.
        """
        total = 0
        product_ids = list(map(int, self.cart.keys()))
        products = Product.objects.filter(id__in=product_ids)
        product_map = {str(product.id): product for product in products}

        for product_id, quantity in self.cart.items():
            product = product_map.get(product_id)
            if not product:
                continue
            if product.on_sale:
                total += product.price_after_discount * quantity
            else:
                total += product.price * quantity

        return total
    

    def _update_user_cart(self):
        """
        Save the current cart state to the authenticated user's profile.
        """
        if self.request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=self.request.user)
                profile.saved_cart = json.dumps(self.cart)
                profile.save()
            except Profile.DoesNotExist:
                pass

    def restore_cart_from_profile(self):
        """
        Load saved cart from user profile into session after login.
        """
        if self.request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=self.request.user)
                if profile.saved_cart:
                    self.cart = json.loads(profile.saved_cart)
                    self.session[self.SESSION_KEY] = self.cart
                    self.session.modified = True
            except Profile.DoesNotExist:
                pass
