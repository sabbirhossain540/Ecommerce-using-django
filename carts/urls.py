from django.urls import path
from .views import cart_home

urlpatterns = [
   path('', cart_home , name="cart"),
   #path('cart_update/', cart_update, 'cart_update'),
]