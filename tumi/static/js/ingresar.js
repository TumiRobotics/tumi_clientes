function ingresarUsuario()
{
    fetch(`/tumi/consultarUsuario?username=${document.getElementById('username').value}&contraUser=${document.getElementById('contraUser').value}`)
    .then(response => response.json() )
    .then(data => {
        console.log(data)
    })
}

document.addEventListener('DOMContentLoaded',()=>{
    console.log('Todo se ha cargado')
})