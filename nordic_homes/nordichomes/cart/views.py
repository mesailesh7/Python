from django.shortcuts import render

# Create your views here.
from .cart import Cart

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    # print("this is cart", cart.cart)
    return render(request,'cart/menu_cart.html')