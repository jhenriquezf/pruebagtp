from django.urls import path
from .admin import get_producto_price

urlpatterns = [
    path('<int:object_id>/get_producto_price/', get_producto_price, name='get_producto_price'),
]

