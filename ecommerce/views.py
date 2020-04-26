from django.http import HttpResponse
from django.shortcuts import render

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
    context = {
        "title" : "Contact Page",
        "content" : "Welcome To the Contact page"
    }
    return render(request, "home_page.html", context)




def index_old(request):
    html_ = """
    

    """
    return HttpResponse(html_)