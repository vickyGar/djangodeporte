from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('product-single/', productsingle, name='product-single'),
    path('shop/', shop, name='shop'),
]
