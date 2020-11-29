from django.shortcuts import render
from django.conf import settings
from mainapp.models import ProductCategory, Product
import os
import json


def main(request):
    products = Product.objects.all()
    content= {
        'title': 'Главная',
        "products": products
    }
    return render(request,'mainapp/index.html',content)

def products(request,pk=None):
    links_menu = ProductCategory.objects.all()
    file_content = os.path.join(settings.BASE_DIR, "products.json")
    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
    }
    return render(request,'mainapp/products.html',content)

def contact(request):
    locations = []
    file_content = os.path.join(settings.BASE_DIR, "contacts.json")
    with open(file_content) as fc:
        file_contact = fc.read()
        locations = json.loads(file_contact)
    content= {
        'title': 'Продукты',
        'locations': locations
    }
    return render(request,'mainapp/contact.html',content)

def products_all(request):
    links_menu = ProductCategory.objects.all()
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request,'mainapp/products.html',content)

def products_home(request):
    links_menu = ProductCategory.objects.all()
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request,'mainapp/products.html',content)
