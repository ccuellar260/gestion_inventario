from django.shortcuts import render


def venta_index(request):
    # Logic to retrieve and display products
    return render(request, 'ventas/venta_index.html')

def venta_create(request):
    # Logic to create a new product
    return render(request, 'ventas/venta_create.html')
