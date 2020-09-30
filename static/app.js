const botonBuscar = document.querySelector('#buscar');

if(botonBuscar){
    botonBuscar.addEventListener('click', function(e){   
         
        botonBuscar.innerHTML = `<div class="spinner-border text-light" role="status">
        <span class="sr-only">calgando</span>
        </div>`;
         
        e.stopPropagation();
    });
}
