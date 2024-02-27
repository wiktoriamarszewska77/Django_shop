from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    ordering = ['-data_added']
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_product.html'

class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    template_name = 'add_product.html'
    fields = ['seller', 'name', 'brand', 'category', 'price', 'data_added', 'description',
              'image', 'stock_quantity', 'available']

    def form_valid(self, form):
        form.instance.company = self.request.user
        return super().form_valid(form)

