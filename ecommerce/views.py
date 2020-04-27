from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import ContactForm, LoginForm

def index(request):
    context = {
        "title" : "Index Page",
        "content" : "Welcome To the Home page"
    }
    return render(request, "home_page.html", context)

def about(request):
    context = {
        "title" : "About Page",
        "content" : "Welcome To the About page"
    }
    return render(request, "home_page.html", context)

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


def login_page(request):
    form = LoginForm(request.POST or None)
    #print(request.user.is_authenticated())

    context = {
        "form" : form
    }

    if form.is_valid():
        print(form.cleaned_data)
        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("error")

    return render(request, "auth/login.html", context)


def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request, "auth/register.html", {})






