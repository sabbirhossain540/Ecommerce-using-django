from django.shortcuts import render, get_object_or_404
from django.http import Http404
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

    #-------------- Retrive Or Filter Data Process 1 -----------------#
    #instance = get_object_or_404(Product, pk=pk)


    #-------------- Retrive Or Filter Data Process 2 -----------------#
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     raise Http404("Product Doesn't Exist")
    # except:
    #     print("Huu???")

    #-------------- Retrive Or Filter Data Process 3 -----------------#
    qs = Product.objects.filter(id = pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product Not Exists")

    

    context = {
        'object':instance
    }
    return render(request, "product/detail.html", context)


