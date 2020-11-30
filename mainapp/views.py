from django.shortcuts import render
<<<<<<< HEAD

def main(request):
    content= {
        'title': 'Главная'
    }
    return render(request,'mainapp/index.html',content)

def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'Офис'},
        {'href': 'products_modern', 'name': 'Модерн'},
        {'href': 'products_classic', 'name': 'Классика'},
    ]
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
=======
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
>>>>>>> Home_3
    }
    return render(request,'mainapp/products.html',content)

def contact(request):
<<<<<<< HEAD
    content= {
        'title': 'Контакты'
=======
    locations = []
    file_content = os.path.join(settings.BASE_DIR, "contacts.json")
    with open(file_content) as fc:
        file_contact = fc.read()
        locations = json.loads(file_contact)
    content= {
        'title': 'Продукты',
        'locations': locations
>>>>>>> Home_3
    }
    return render(request,'mainapp/contact.html',content)

def products_all(request):
<<<<<<< HEAD
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'Офис'},
        {'href': 'products_modern', 'name': 'Модерн'},
        {'href': 'products_classic', 'name': 'Классика'},
    ]
=======
    links_menu = ProductCategory.objects.all()
>>>>>>> Home_3
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request,'mainapp/products.html',content)

def products_home(request):
<<<<<<< HEAD
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'Офис'},
        {'href': 'products_modern', 'name': 'Модерн'},
        {'href': 'products_classic', 'name': 'Классика'},
    ]
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request,'mainapp/products.html',content)

def products_office(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'Офис'},
        {'href': 'products_modern', 'name': 'Модерн'},
        {'href': 'products_classic', 'name': 'Классика'},
    ]
=======
    links_menu = ProductCategory.objects.all()
>>>>>>> Home_3
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request,'mainapp/products.html',content)
<<<<<<< HEAD

def products_modern(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'Офис'},
        {'href': 'products_modern', 'name': 'Модерн'},
        {'href': 'products_classic', 'name': 'Классика'},
    ]
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request,'mainapp/products.html',content)

def products_classic(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'Офис'},
        {'href': 'products_modern', 'name': 'Модерн'},
        {'href': 'products_classic', 'name': 'Классика'},
    ]
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request,'mainapp/products.html',content)

# Create your views here.
=======
>>>>>>> Home_3
