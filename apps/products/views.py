from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponseRedirect
from apps.products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


User = get_user_model()


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


def products(request, category_id=None, page_number=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        "title": "Store - каталог",
        "categories": ProductCategory.objects.all(),
        "products": products_paginator,
    }

    return render(
        request=request,
        template_name="products/products.html",
        context=context,
    )


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
