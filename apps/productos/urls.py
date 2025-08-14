from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_index, name='productos_index'),
    path('create', views.producto_create, name='productos_create')
]
