from django.urls import path

from codigo.views import inicio, informacion,catalogo_productos,agregar_producto,eliminar,modificar,registrar,carrito_compras,agregar_carrito,eliminar_producto,restar_producto,limpiar_carrito,detalle_compras,generarBoleta,historial,sumar_carrito

urlpatterns=[
    path('', inicio, name='inicio'), #comillas simples vacias es para que sea la pagina inicial
    path('informacion/', informacion, name='informacion'),
    path('catalogo_productos/', catalogo_productos, name='catalogo_productos'),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('eliminar/<codigo>', eliminar, name="eliminar"),
    path('modificar/<codigo>', modificar, name="modificar"),
    #Registo usuario
    path('registrar/', registrar, name="registrar"),
    #Carrito de compras.
    path('carrito_compras/',carrito_compras,name="carrito_compras"),
    path('agregar_carrito/<codigo>',agregar_carrito,name="agregar_carrito"),
    path('eliminar_producto/<codigo>', eliminar_producto, name="eliminar"),
    path('restar_producto/<codigo>', restar_producto, name="restar"),
    path('limpiar_carrito/', limpiar_carrito, name="limpiar"),
    path('sumar_carrito/<codigo>', sumar_carrito, name="sumar_carrito"),
    #Detalle de compras.
    path('detalle_compras/', detalle_compras,name="detalle_compras"),
    path('generarBoleta/', generarBoleta ,name="generarBoleta"),
    #Hisotrial de compras.
    path('historial/', historial,name="historial"),
]