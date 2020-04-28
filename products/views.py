from django.shortcuts import render, get_object_or_404

# Create your views here.


#Class Based View
from django.views.generic import ListView, DetailView
from .models import Product

#------------------- List View Start Here ---------------------#
#Class Based View
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


#-------------------- Detail View Start Here -----------------------#
#Class Based View
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"


    ## Every List view have this function 
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


#Function Based View

def product_detail_view(request, pk, *args, **kwargs):
    #instance = Product.objects.get(pk=pk)

    instance = get_object_or_404(Product, pk=pk)

    context = {
        'object':instance
    }
    return render(request, "product/detail.html", context)


