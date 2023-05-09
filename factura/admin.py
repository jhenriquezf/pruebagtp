from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .models import Producto, Factura, DetalleFactura

class DetalleFacturaInline(admin.TabularInline):
    model = DetalleFactura
    extra = 1

class FacturaAdmin(admin.ModelAdmin):
    inlines = [DetalleFacturaInline]
    list_display = ('id', 'cliente', 'fecha', 'total')
    list_filter = ('fecha',)
    search_fields = ('cliente__nombre',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_producto_price/', self.get_producto_price, name='get_producto_price'),
        ]
        return custom_urls + urls


    def get_producto_price(request, object_id):
        producto_id = request.GET.get('producto_id')
        try:
            producto = Producto.objects.only('precio_unitario').get(pk=producto_id)
            precio = str(producto.precio_unitario)
        except Producto.DoesNotExist:
            precio = ''
        data = {'precio': precio}
        return JsonResponse(data)

    class Media:
        js = ['js/jquery.min.js', 'js/admin.js']

admin.site.register(Producto)
admin.site.register(Factura, FacturaAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
]
