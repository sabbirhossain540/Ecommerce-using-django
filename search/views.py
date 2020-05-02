
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from products.models import Product
# Create your views here.

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        print(query)

        if query is not None:
            return Product.objects.search(query)
            #This Handle From Product Model
            # lookups = Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
            # return Product.objects.filter(lookups).distinct()

        return Product.objects.featured()
        

    '''
    __icontains = field contains this
    __iexact = Fields is exactly this

    '''


