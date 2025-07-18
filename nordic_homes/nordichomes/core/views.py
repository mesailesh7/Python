from django.shortcuts import render
# we are import Q so that can search in multiple fields
from django.db.models import Q
# we have import product in here so that from the backedn we can pass it to the frontend just like props in react
from product.models import Product,Category

# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request, 'core/frontpage.html',{'products':products})
# by giving context to the frontpage function we can it the frontpage .html data from the backend




def signup(request):
    return render(request, 'core/signup.html')

def login(request):
    return render(request, 'core/login.html')




def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    # this is to only show the products that user click on categories
    # using GET.get('category') we can get the category from url and default is '' empty
    active_category = request.GET.get('category','')

    # this code to filter the category and show only the products that belongs to the categories
    if active_category:
        products = products.filter(category__slug=active_category)
    # request.GET.get('query','') query is the same name which we put it in shop.html input field
    query = request.GET.get('query','')

    # name__icontains so that we don't want to be sensative to capital or lower letter and Q() | Q() so that we can search it in multiple fields

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {'products':products,'categories':categories,'active_category':active_category}

    return render(request,'core/shop.html', context)