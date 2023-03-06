from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MenuItem


def redirecter(request):
    return redirect(request, 'home')


def index(request, menu_url=None):
    print(menu_url)
    menu = MenuItem.objects.all()
    context = {
        'menu': menu
    }
    # return redirect(reverse('/contact/', kwargs=context))
    return render(request, 'index.html', context)
