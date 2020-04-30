from django.urls import path

from .views import (
                            product_list_view, 
                            ProductListView, 
                            ProductDetailView, 
                            product_detail_view, 
                            ProductFeaturedListView, 
                            ProductFeaturedDetailView,
                            ProductDetailSlugView
                            )

urlpatterns = [

    #Listview Url Pattern
     path('',ProductListView.as_view() , name="products"),
    # path('products-fbv/',product_list_view , name="product_fbv"),

    #Product Detail Slug Based View
    path('<slug:slug>',ProductDetailSlugView.as_view() , name="products"),

    #DetailView Url Pattern 
    path('<int:pk>',ProductDetailView.as_view() , name="products_detail"),
    # path('products-fbv/<int:pk>',product_detail_view , name="product_detail_fbv"),

    #Product Feature Url
    path('featured/',ProductFeaturedListView.as_view() , name="fetaured"),
    path('featured/<int:pk>',ProductFeaturedDetailView.as_view() , name="featured_detail"),
]

