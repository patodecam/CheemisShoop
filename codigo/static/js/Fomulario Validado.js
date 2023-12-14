 //funcion que valida un formulario
$(function(){
    
    $("#contactame").validate({

        rules:{
            nombre:{
                required:true
            },
            apellido:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            fono:{
                required:true
            },
            
            fecha:{
                required:true
            },
            genero:{
                required:true
            },
            mascota:{
                required:true
            },
            mensaje:{
                required:true,
                minlength: 25
            }
        },//rules
        messages:{
            nombre:{
                required:'Ingrese su nombre',
                minlength:'Caracteres insuficientes (3)'
            },
            apellido:{
                required:'Ingrese su apellido',
                minlength:'Caracteres insuficientes (3)'
            },
            correo:{
                required:'Ingrese correo electrónico',
                email:'Formato de correo no válido'
            },
            fono:{
                required:'Ingrese número de teléfono',
                minlength:'Digitos insuficientes (9)'
            },
            fecha:{
                required:'Ingrese una fecha',
                max:'Seleccione una fecha válida,tiene que ser mayor de 18 años '
            },
            genero:{
                required:'Seleccione su genero',
                combo:'Seleccione genero'
            },
            mascota:{
                required:'Seleecione su tipo de mascota',
                check:'Seleccione tipo de mascota.'
            },
            mensaje:{
                required:'Tiene que escribir un mensaje',
                minlength:'Digitos insuficientes (25)'
            }
        },
    })
});


 //Fetch para llamara a la api de divisas.
        

let url='https://mindicador.cl/api/';
    fetch(url)
    .then(Response=>Response.json())
    .then(data=>mostrarData(data))
    .catch(error=>console.log(error))
const mostrarData=(data)=>{
    console.log(data)
    console.log(data.length)
    let body=""
    body+=  `<tr>
                <td>${data.ivp.codigo}</td>
                <td>${data.ivp.nombre}</td>
                <td>${"$"+data.ivp.valor}</td>
                <td>${data.ivp.fecha}</td>
                </tr>
                <tr>
                <td>${data.uf.codigo}</td>
                <td>${data.uf.nombre}</td>
                <td>${"$"+data.uf.valor}</td>
                <td>${data.uf.fecha}</td>
                </tr>
                <tr>
                <td>${data.dolar.codigo}</td>
                <td>${data.dolar.nombre}</td>
                <td>${"$"+data.dolar.valor}</td>
                <td>${data.dolar.fecha}</td>
                </tr>
                <tr>
                <td>${data.euro.codigo}</td>
                <td>${data.euro.nombre}</td>
                <td>${"$"+data.euro.valor}</td>
                <td>${data.euro.fecha}</td>
                </tr>
                <tr>
                <td>${data.utm.codigo}</td>
                <td>${data.utm.nombre}</td>
                <td>${"$"+data.utm.valor}</td>
                <td>${data.utm.fecha}</td>
                </tr>`
    document.getElementById('data').innerHTML=body
}

//Funciones Dom

function uppertext(texto){
    const x = texto;
    x.value= x.value.toUpperCase();

}