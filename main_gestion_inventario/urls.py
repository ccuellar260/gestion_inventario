from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('apps.productos.urls')),
    path('ventas/', include('apps.ventas.urls')),
]
