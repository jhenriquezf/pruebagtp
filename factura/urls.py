from django.urls import path
#from factura import admin
from . import views


urlpatterns = [
   path('get_producto_price/<int:producto_id>/', views.get_producto_price, name='get_producto_price'),
]
