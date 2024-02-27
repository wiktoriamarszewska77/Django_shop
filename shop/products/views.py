from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Company



class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    ordering = ['-data_added']
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_product.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = ['name', 'brand', 'category', 'price', 'data_added', 'description',
              'image', 'stock_quantity', 'available']

    def form_valid(self, form):
        company = Company.objects.get(user=self.request.user)
        form.instance.seller = company
        return super().form_valid(form)


