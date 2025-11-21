from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "crud/product_create_form.html"
    success_url = reverse_lazy("list")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "crud/product_update_form.html"
    success_url = reverse_lazy("list")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("list")

class ProductDetailView(DetailView):
    model = Product