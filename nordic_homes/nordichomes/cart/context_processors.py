# this is done to make it globally available for all the front end pages or in cart because we want to get quty or price or the cart information globally in the front end


from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}