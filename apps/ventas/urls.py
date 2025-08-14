from django.urls import path
from . import views

urlpatterns = [
    path('', views.venta_index, name='ventas_index'),
    path('create', views.venta_create, name='ventas_create')
]
