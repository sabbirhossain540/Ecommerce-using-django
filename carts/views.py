from django.shortcuts import render

# Create your views here.

def cart_home(request):
    print(request.session)
    #print(dir(request.session))
    key = request.session.session_key
    print(key)
    #request.session.set_expiry(300)


    return render(request, "carts/home.html")
