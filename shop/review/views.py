from .models import Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from products.models import Product
from django.shortcuts import get_object_or_404
from django.urls import reverse


class ReviewProductView(ListView):
    model = Review
    template_name = "review_product.html"
    context_object_name = "reviews"

    def get_queryset(self):
        product_id = self.kwargs.get("product_id")
        queryset = Review.objects.filter(product_id=product_id)
        return queryset


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "add_review.html"
    fields = ["comment", "rating"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        product_id = self.kwargs["product_id"]
        form.instance.product = get_object_or_404(Product, id=product_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail-product", kwargs={"pk": self.kwargs["product_id"]})


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    template_name = "add_review.html"
    fields = ["comment", "rating"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        review = self.get_object()
        form.instance.product = get_object_or_404(Product, id=review.product.id)
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "add_review.html"
    fields = ["comment", "rating"]

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user


class ReviewUserView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "user_reviews.html"
    context_object_name = "reviews"

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(user=user)
