"""
URL configuration for nordichomes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# this import are used
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

#  this is bringing front end html page and to redirect to the url
from core.views import frontpage,shop, signup,login
from product.views import product


# This is we are importing view from cart
from cart.views import add_to_cart
urlpatterns = [
    path("admin/", admin.site.urls),
    # After I created a base.html file in the core folder I redirected all the urs  request to the core base.html and frontpage is being importted from frontpage/
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('shop/', shop, name='shop'),
    # <slug:slug> left slug means we want a slug and right slug is the  name (which we are getting for products.view)
    path('shop/<slug:slug>/', product, name='product'),

    # cart
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

    # Please always put it in the end
    path("__reload__/", include("django_browser_reload.urls")),
]
