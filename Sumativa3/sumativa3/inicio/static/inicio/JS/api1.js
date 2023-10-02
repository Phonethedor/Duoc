$(document).ready(function(){
    $.get('https://dog.ceo/api/breeds/image/random', function(datos){
        $('#img_api').append("<img id='img_animal' src="+datos.message+">");
    }, 'json');
});