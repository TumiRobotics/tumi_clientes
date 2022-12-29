function ingresarUsuario()
{
    fetch(`/tumi/consultarUsuario?username=${document.getElementById('username').value}&contraUser=${document.getElementById('contraUser').value}`)
    .then(response => response.json() )
    .then(data => {
        if(data.resp === '200')
        {
            console.log('Datos de usuario correctos')
            document.getElementById('mensajeError').innerHTML=''
            document.getElementById('accesoCredenciales').style.display = 'none'
            document.getElementById('accesoCodigo').style.display = 'block'
        }
        else if(data.resp === '404')
        {
            console.log('Datos de usuario erroneos')
            document.getElementById('mensajeError').innerHTML='Datos Erroneos!'
        }
    })
}

function verificarCodigo()
{
    fetch(`/tumi/verificarCodigoUsuario?codigoCelular=${document.getElementById('codigoUsuario').value}`)
    .then(response => response.json())
    .then(data => {
        if(data.resp === '200')
        {
            console.log('Usuario accedido')
            window.location.assign('/tumi/dashboard')
        }
        else if(data.resp === '404')
        {
            console.log('Datos de usuario erroneos')
            document.getElementById('codigoError').innerHTML='Codigo erroneo!'
        }
    })
}

document.addEventListener('DOMContentLoaded',()=>{
    console.log('Todo se ha cargado')
})