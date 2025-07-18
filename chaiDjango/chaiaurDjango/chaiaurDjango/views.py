from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'website/index.html')
    # return HttpResponse("Hello, world. You're at chai aur Django home page.")


def about(request):
    return HttpResponse("About You")

def contact(request):
    return HttpResponse("Contact You")

