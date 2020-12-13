from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Users
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def user_create(request):
    if request.method == "POST":
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("admin:users"))

    user_form = ShopUserRegisterForm()
    content = {
        "update_form": user_form
    }
    return render(request, "adminapp/user_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def users(requset):
    users_list = ShopUser.objects.all().order_by("-is_active")
    content = {
        "objects": users_list,
    }
    return render(requset, "adminapp/users.html", content)


def user_update(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("admin:user_update", args=[edit_user.pk]))
    edit_form = ShopUserAdminEditForm(instance=edit_user)
    content = {
        "update_form": edit_form
    }
    return render(request, "adminapp/user_update.html", content)


def user_delete(request, pk):
    user_item = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        if user_item.is_active:
            user_item.is_active = False
        else:
            user_item.is_active = True
        user_item.save()
        return HttpResponseRedirect(reverse("admin:users"))
    content = {
        "user_to_delete": user_item
    }
    return render(request, "adminapp/user_delete.html", content)


# Category

def category_create(requset):
    pass


def categories(requset):
    categories_list = ProductCategory.objects.all().order_by("-is_active")
    content = {
        "objects": categories_list
    }

    return render(requset, "adminapp/categories.html", content)


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


# Products

def product_create(requset, pk):
    pass


def products(requset, pk):
    category_item = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category=category_item)
    content = {
        "objects": product_list,
        "category": category_item
    }
    return render(requset, "adminapp/products.html/", content)


def product_read(requset, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass
