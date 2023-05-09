django.jQuery(document).ready(function() {
  // Seleccionar todos los selects que tengan el nombre "-producto"
  $('select[name$="-producto"]').each(function() {
    // Obtener el select actual
    var select = $(this);
    // Obtener el precio_unitario de la fila actual
    var precio_field = select.closest('tr').find('input[name$="-precio_unitario"]');
    // Función para hacer la llamada AJAX y actualizar el precio
    var updatePrecio = function() {
      var producto_id = select.val();
      $.ajax({
        url: '/factura/get_producto_price/' + producto_id + '/',
        data: {
          'producto_id': producto_id,
        },
        success: function(data) {
          precio_field.val(data.precio);
        },
      });
    }
    // Ejecutar la función en la carga inicial de la página
    updatePrecio();
    // Ejecutar la función cada vez que se cambia el valor del select
    select.change(updatePrecio);
  });
});
