//Valida formulario popup.

$(function(){
    
    $("#doname").validate({

        rules:{
            nombrecom:{
                required:true
            },
            TipoBanco:{
                required:true
            },
            TipoCuenta:{
                required:true
            },
            cuenta:{
                required:true
            },
            mail:{
                required:true,
                email:true
            },
            monto:{
                required:true
            }
        },//rules
        messages:{
            nombrecom:{
                required:'Ingrese su nombre completo',
                minlength:'Caracteres insuficientes (3)'
            },
            TipoBanco:{
                required:'Seleccione su banco',
                combo:'Seleccione banco'
            },
            TipoCuenta:{
                required:'Seleecione su tipo de cuenta',
                check:'Seleccione tipo de cuenta'
            },
            cuenta:{
                required:'Ingrese número de cuenta',
                minlength:'Digitos insuficientes (8)',
                maxlength:'Digitos insuficientes (16)'

            },
            
            mail:{
                required:'Ingrese correo electrónico',
                email:'Formato de correo no válido'
            },
            monto:{
                required:"Ingrese una monto valido",
                min:"Ingrese un monto mayor a  $0"
            }

        },
    })
});

//funcion que permite crear una carta
function CrearCarta(){
    var TipoBanco="";
    var TipoCuenta="";
    var a=document.getElementById("nombrecom").value;
    var b=parseInt(document.getElementById("cuenta").value);
    var c= parseInt(document.getElementById("monto").value);
    var d=document.getElementById("mail").value;

    var elementoTipoBanco = document.getElementById('TipoBanco');
    var indiceSeleccionado = elementoTipoBanco.selectedIndex; 
    var tib=elementoTipoBanco.options[indiceSeleccionado].text;

    var elementoTipoCuenta = document.getElementById('TipoCuenta');
    var indiceSeleccionado = elementoTipoCuenta.selectedIndex;
    var tic=elementoTipoCuenta.options[indiceSeleccionado].text;

        var cadena= 
            "Donacion a la Fundacion Cheemis Shop:" + "\n"
            + "Nombre: " + a + "\n"
            + "Correo: " + d + "\n" 
            + "Monto $: " + c + "\n"
            + "Banco: " + tib + "\n"
            + "Tipo de Cuenta: " + tic+"\n"
            "Muchas gracias por donar a esta causa.";

        document.getElementById("mensaje").value=cadena;
    }

//Funciones DOM

function colorBrown(obj){
    obj.style.backgroundColor='brown';

}

function colorBlanco(obj){
    obj.style.backgroundColor='white';

}

function uppertext(texto){
    const x = texto;
    x.value= x.value.toUpperCase();

}