

//Anima y filtra los elementos dle catalogo.
$(document).ready(function(){
    //filtrando
    $('.item_categoria').click(function(){
        var catProduct = $(this).attr('category');
        console.log(catProduct);

        //animacion
        $('.item_producto').css('transform', 'scale(0)')
        function esconderProduct(){
            $('.item_producto').hide();

        }setTimeout(esconderProduct,400);

        function mostrarProducto(){
            $('.item_producto[category="'+catProduct+'"]').show();
            $('.item_producto[category="'+catProduct+'"]').css('transform', 'scale(1)')

        }setTimeout(mostrarProducto,400);

    });

    $('.item_categoria[category="all"]').click(function(){
        function mostrarTodo(){
            $('.item_producto').show();
            $('.item_producto').css('transform', 'scale(1)')

        }setTimeout(mostrarTodo,400);

    });

});

