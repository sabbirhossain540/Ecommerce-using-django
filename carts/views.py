from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product

# Create your views here.

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('New Cart Created')
    return cart_obj

def cart_home(request):

    # cart_id = request.session.get("cart_id", None)
    # qs = Cart.objects.filter(id=cart_id)
    # if qs.count() == 1:
    #   print("Cart Id exists")
    #   cart_obj = qs.first()
    #   if request.user.is_authenticated and cart_obj.user is None:
    #     cart_obj.user = request.user
    #     cart_obj.save()
    # else:
    #   #cart_obj = cart_create()
    #   cart_obj = Cart.objects.new(user=request.user)
    #   request.session['cart_id'] = cart_obj.id
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
      total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()

    return render(request, "carts/home.html")


def cart_update(request):
  
  product_id = 3
  product_obj = Product.objects.get(id=product_id)
  print(product_obj)
  cart_obj, new_obj = Cart.objects.new_or_get(request)
  cart_obj.products.add(product_obj)
  return redirect(product_obj.get_absolute_url)
  


