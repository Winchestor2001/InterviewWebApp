from django.contrib import admin


from django.contrib import admin
from django import forms

from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

