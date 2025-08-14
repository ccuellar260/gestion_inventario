from django.shortcuts import render

def producto_index(request):
    # Logic to retrieve and display products
    return render(request, 'productos/producto_index.html')

def producto_create(request):
    # Logic to create a new product
    return render(request, 'productos/producto_create.html')