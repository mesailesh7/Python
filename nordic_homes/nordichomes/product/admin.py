from django.contrib import admin

# Register your models here.
# first import the model and then import it to the category
from .models import Category, Product
admin.site.register(Category)
admin.site.register(Product)