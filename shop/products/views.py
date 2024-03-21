from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Company
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ProductListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"
    ordering = ["-data_added"]
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail_product.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "add_product.html"
    fields = [
        "name",
        "brand",
        "category",
        "price",
        "data_added",
        "description",
        "image",
        "stock_quantity",
        "available",
    ]

    def form_valid(self, form):
        company = Company.objects.get(user=self.request.user)
        form.instance.seller = company
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = "add_product.html"
    fields = [
        "name",
        "brand",
        "category",
        "price",
        "data_added",
        "description",
        "image",
        "stock_quantity",
        "available",
    ]

    def form_valid(self, form):
        company = Company.objects.get(user=self.request.user)
        form.instance.seller = company
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        company = Company.objects.get(user=self.request.user)
        return company == product.seller


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "delete_product.html"
    success_url = "/user/products/"

    def test_func(self):
        product = self.get_object()
        company = Company.objects.get(user=self.request.user)
        return company == product.seller


class CategoryProductListView(ListView):
    model = Product
    template_name = "category.html"
    context_object_name = "products"

    def get_queryset(self):
        category = self.kwargs["category"]
        return Product.objects.filter(category=category)


class BrandProductListView(ListView):
    model = Product
    template_name = "brand.html"
    context_object_name = "products"

    def get_queryset(self):
        brand = self.kwargs["brand"]
        return Product.objects.filter(brand=brand)


class UserProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "user_products.html"
    context_object_name = "products"

    def get_queryset(self):
        user = self.request.user
        company = get_object_or_404(Company, user=user)
        return Product.objects.filter(seller=company)
