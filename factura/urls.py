from django.urls import path
from .admin import FacturaAdmin

urlpatterns = [
    path('get_producto_price/', FacturaAdmin.get_producto_price, name='get_producto_price'),
]
