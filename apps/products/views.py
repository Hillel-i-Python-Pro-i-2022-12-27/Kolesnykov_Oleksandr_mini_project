from django.shortcuts import render
from apps.products.models import Product, ProductCategory


def index(request):
    context = {
        "title": "Store",
        "is_promotion": True,
    }
    return render(
        request=request,
        template_name="index.html",
        context=context,
    )


def products(request):
    context = {
        "title": "Store - каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }
    return render(
        request=request,
        template_name="products/products.html",
        context=context,
    )
