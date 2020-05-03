from django.shortcuts import render

# Create your views here.

def cart_home(request):
    card_id = request.session.get("cart_id", None)

    if card_id is None:
        print('Create New Cart')
        request.session['cart_id'] = 13
    else:
        print("Card is Exits")


    return render(request, "carts/home.html")
