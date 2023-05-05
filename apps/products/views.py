from django.shortcuts import render


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
    }
    return render(
        request=request,
        template_name="products/products.html",
        context=context,
    )
