from django.shortcuts import render

# Create your views here.


#Class Based View
from django.views.generic.list import ListView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "product/product_list.html"


    ## Every List view have this function 
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


#Function Based View

def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        'object_list':queryset
    }
    return render(request, "product/product_list.html", context)


