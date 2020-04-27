from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

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






