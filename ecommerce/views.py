from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "home_page.html", {})




def index_old(request):
    html_ = """
    

    """
    return HttpResponse(html_)