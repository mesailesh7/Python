from django.shortcuts import render, get_object_or_404

from product.models import Product


# Create your views here.
def product(request, slug):
    # we are gonna get 404 error if the product doesn't exist
    product = get_object_or_404(Product,slug=slug)

    return render(request,'product/product.html',{'product':product})