from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm, LoginForm, RegisterForm

def index(request):
    context = {
        "title" : "Index Page",
        "content" : "Welcome To the Home page"
    }

    if request.user.is_authenticated:
        context["premeum_content"] = "You are So Lucky"

    return render(request, "home_page.html", context)

#------------- End Index Function -----------------#

def about(request):
    context = {
        "title" : "About Page",
        "content" : "Welcome To the About page"
    }
    return render(request, "home_page.html", context)

#------------- End About Function -----------------#

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "Contact Page",
        "content" : "Welcome To the Contact page",
        "form" : contact_form

    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST)
    return render(request, "contact/view.html", context)


#------------- End Contact Function -----------------#

def login_page(request):
    form = LoginForm(request.POST or None)
    #print(request.user.is_authenticated())

    context = {
        "form" : form
    }

    if form.is_valid():
        #print(form.cleaned_data)
        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            print("error")

    return render(request, "auth/login.html", context)

#------------- End Login Function -----------------#

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)

#------------- End Register Function -----------------#




