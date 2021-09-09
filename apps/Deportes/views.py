from django.shortcuts import render
from.models import *

# Create your views here.

def index(request):
    allproduct = garment.objects.all()
    return render(request, 'index.html' , {'allproduct' :allproduct})
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')
def about(request):
    return render(request, 'about.html')
def cart(request):
    return render(request, 'cart.html')
def blogsingle(request):
    return render(request, 'blog-single.html')
def checkout(request):
    return render(request, 'checkout.html')
def productsingle(request):
    return render(request, 'product-single.html')
def shop(request):
    return render(request, 'shop.html')





