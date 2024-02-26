from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView



class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    ordering = ['-data_added']
    paginate_by = 2

