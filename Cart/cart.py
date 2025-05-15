from Ecommerce_Core.models import Product,Profile



class Cart():
    def __init__(self,request):
        self.session = request.session
        self.request = request

        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}

        cart = self.session.get('session_key')

        self.cart = cart



    def add_cart(self,pk,quantity=1):

        product_id = str(pk)
        product_quantity = quantity
          
        self.cart[product_id] = product_quantity

        self.session.modified = True

        if self.request.user.is_authenticated:
            profile = Profile.objects.filter(user=self.request.user)
            new_cart = str(self.cart)
            profile.update(saved_cart=new_cart)

    # Use the same func for updating 


    def delete_cart(self,pk):
        product_id = str(pk)
        del(self.cart[product_id])

        self.session.modified = True
        if self.request.user.is_authenticated:
            profile = Profile.objects.filter(user=self.request.user)
            profile.update(saved_cart=str(self.cart))


    def get_quants(self):
        quants = self.cart

        return quants



    def __len__(self):
        return len(self.cart)
    
        


    def get_products(self):

        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        return products
    
    def get_total(self):
        total = 0
        for key,value in self.cart.items:
            product = Product.objects.get(id=int(key))
            if product.on_sale:
                total += product.price_after_discount * value

            else:
                total += product.price * value

        return total
    

    


    


        





    
        