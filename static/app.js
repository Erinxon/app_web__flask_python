const botonBuscar = document.querySelector('#buscar');


if(botonBuscar){
    botonBuscar.addEventListener('click', function(e){
        console.log('Click en buscar pokemon');
        botonBuscar.innerHTML = `<div class="spinner-border text-light" role="status">
        <span class="sr-only">calgando</span>
        </div>`;
        botonBuscar.disabled = false
        e.stopPropagation();
    });
}
