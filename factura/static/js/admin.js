$(document).ready(function() {
    $('select[name$="-producto"]').change(function() {
      var producto_id = $(this).val();
      var precio_field = $(this).closest('tr').find('input[name$="-precio_unitario"]');
      $.ajax({
        url: '/admin/facturas/get_producto_price/',
        data: {
          'producto_id': producto_id,
        },
        success: function(data) {
          precio_field.val(data.precio);
        },
      });
    });
  });
  