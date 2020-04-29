"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from . import views

from products.views import (
                            product_list_view, 
                            ProductListView, 
                            ProductDetailView, 
                            product_detail_view, 
                            ProductFeaturedListView, 
                            ProductFeaturedDetailView
                            )

urlpatterns = [
    path('',views.index , name="home"),
    path('about/',views.about , name="about"),
    path('contact/',views.contact , name="contact"),
    path('login/',views.login_page , name="login"),
    path('register/',views.register_page , name="register"),

    #Listview Url Pattern
    path('products/',ProductListView.as_view() , name="products"),
    path('products-fbv/',product_list_view , name="product_fbv"),

    #DetailView Url Pattern 
    path('products/<int:pk>',ProductDetailView.as_view() , name="products_detail"),
    path('products-fbv/<int:pk>',product_detail_view , name="product_detail_fbv"),

    #Product Feature Url
    path('featured/',ProductFeaturedListView.as_view() , name="fetaured"),
    path('featured/<int:pk>',ProductFeaturedDetailView.as_view() , name="featured_detail"),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
