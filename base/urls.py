from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='redirecter'),
    path('menu/<path:menu_url>/', views.index, name='home'),
]