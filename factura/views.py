from django.http import JsonResponse
from .models import Producto

def get_producto_price(request, producto_id):
    try:
        producto = Producto.objects.only('precio_unitario').get(pk=producto_id)
        precio = str(producto.precio_unitario)
    except Producto.DoesNotExist:
        precio = ''
    data = {'precio': precio}
    return JsonResponse(data)
