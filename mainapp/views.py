from django.shortcuts import render

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
    }
    return render(request,'mainapp/products.html',content)

def contact(request):
    content= {
        'title': 'Контакты'
    }
    return render(request,'mainapp/contact.html',content)

def products_all(request):
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

def products_home(request):
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
    content= {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request,'mainapp/products.html',content)

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
