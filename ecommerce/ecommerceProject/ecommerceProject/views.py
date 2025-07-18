from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'ecommerce/index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the polls view about page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the polls view contact page.")