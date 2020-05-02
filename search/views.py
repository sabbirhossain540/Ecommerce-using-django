from django.views.generic import ListView, DetailView
from django.shortcuts import render
from products.models import Product
# Create your views here.

class SearchProductView(ListView):
    template_name = "product/product_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        print(query)

        if query is not None:
            return Product.objects.filter(title__icontains=query)

        return Product.objects.featured()
        

    '''
    __icontains = field contains this
    __iexact = Fields is exactly this

    '''


