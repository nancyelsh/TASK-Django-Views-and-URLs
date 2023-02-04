from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def get_home(request):
    html = 'Welcome to the website!'
    return HttpResponse(f"<h1>{html}</h1>")

def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    print(product)
    my_product_details = f'''{product.name}<br>
                            {product.price}<br>
                            {product.description}'''
    return HttpResponse(my_product_details)
