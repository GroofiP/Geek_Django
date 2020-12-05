from django.shortcuts import render, get_object_or_404
from django.conf import settings

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product
import os
import json


def main(request):
    products_main = Product.objects.all()[0:4]
    content = {
        'title': 'Главная',
        "products": products_main
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 1:
            products_list = Product.objects.all()
            category = {"name": "Все", "pk": 0}
        else:
            # category = ProductCategory.objects.get(pk=pk)
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)

        content = {
            'title': 'Продукты',
            'links_menu': links_menu,
            'products': products_list,
            'category': category,
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[2:4]

    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'products': same_products,
        'basket': basket
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    file_content = os.path.join(settings.BASE_DIR, "mainapp/json/contacts.json")
    with open(file_content) as fc:
        file_contact = fc.read()
        locations = json.loads(file_contact)
        content = {
            'title': 'Продукты',
            'locations': locations
        }
        return render(request, 'mainapp/contact.html', content)
