from django.shortcuts import render
from .models import Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from products.models import Product
from django.shortcuts import get_object_or_404
from django.urls import reverse

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'add_review.html'
    fields = ['comment', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        product_id = self.kwargs['product_id']
        form.instance.product = get_object_or_404(Product, id=product_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-product', kwargs={'pk': self.kwargs['product_id']})

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    template_name = 'add_review.html'
    fields = ['comment', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        product_id = self.kwargs['product_id']
        form.instance.product = get_object_or_404(Product, id=product_id)
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user
