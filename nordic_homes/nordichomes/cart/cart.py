from django.conf import settings
from product.models import Product


# 	•	from django.conf import settings: This line imports the settings object from Django’s configuration, which allows us to access various settings defined in the settings.py file of your Django project. One of these settings is likely CART_SESSION_ID, which is used to identify the shopping cart in the user’s session.
# 	•	from product.models import Product: This imports the Product model from the product app. The Product model represents the products available in your store, and you’ll use it to get information about specific products.
class Cart(object):
    # This line defines the Cart class, which will manage the items in the user’s shopping cart.
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
    # 	•	__init__(self, request): This is the initializer method for the class, which gets called automatically when you create an instance of the Cart class.
    # 	•	self.session = request.session: This stores the current session (a way to persist data between different requests from the same user) in self.session.
    # 	•	cart = self.session.get(settings.CART_SESSION_ID): This tries to get the cart data from the session using the CART_SESSION_ID key. If the cart doesn’t exist yet, it initializes an empty cart.
    # 	•	if not cart:: If the cart doesn’t exist, the code creates an empty dictionary to represent it and saves it in the session under the key CART_SESSION_ID.
    # 	•	self.cart = cart: This stores the cart data in the instance variable self.cart.


    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
    # 	•	__iter__(self): This method allows the Cart object to be iterated over using a loop.
    # 	•	for p in self.cart.keys():: This loops through all the product IDs stored in the cart.
    # 	•	self.cart[str(p)]['product'] = Product.objects.get(pk=p): For each product ID, it retrieves the corresponding Product object from the database and adds it to the cart.

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    # 	•	__len__(self): This method returns the total quantity of all items in the cart by summing the quantities of each product.

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    #     save(self): This method saves the current state of the cart back to the session and marks the session as modified, so Django knows it needs to be saved.

    def add(self,product_id, quantity = 1, update_quantity = False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':1, 'id':product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    #     	•	add(self, product_id, quantity=1, update_quantity=False): This method adds a product to the cart.
    # 	•	product_id = str(product_id): Converts the product ID to a string.
    # 	•	if product_id not in self.cart:: Checks if the product is already in the cart. If not, it adds the product with a default quantity of 1.
    # 	•	if update_quantity:: If update_quantity is True, it updates the quantity of the product in the cart.
    # 	•	self.save(): After modifying the cart, it calls the save method to store the updated cart in the session.

    def remove(self,product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

            # 	•	remove(self, product_id): This method removes a product from the cart if it exists.