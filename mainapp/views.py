import random

from django.shortcuts import render, get_object_or_404
from django.conf import settings

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product
import os
import json


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []

def get_hot_product():
    products_list = Product.objects.all()
    return random.sample(list(products_list),1)[0]

def get_same_products(hot_products):
    return Product.objects.filter(category__pk = hot_products.category.pk).exclude(pk=hot_products.pk)[:3]

def main(request):
    products_main = Product.objects.all()[0:4]
    content = {
        'title': 'Главная',
        "products": products_main,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

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
            'basket': get_basket(request.user)
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'products': same_products,
        'basket': get_basket(request.user),
        'hot_product': hot_product
    }

    return render(request, 'mainapp/products.html', content)

def product(request,pk):
    title = "Продукт"
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.all(),
        'basket': get_basket(request.user),
        "product": get_object_or_404(Product,pk=pk)
    }
    return render(request,"mainapp/product.html", content)

def contact(request):
    file_content = os.path.join(settings.BASE_DIR, "mainapp/json/contacts.json")
    with open(file_content) as fc:
        file_contact = fc.read()
        locations = json.loads(file_contact)
        content = {
            'title': 'Продукты',
            'locations': locations,
            'basket': get_basket(request.user)
        }
        return render(request, 'mainapp/contact.html', content)
