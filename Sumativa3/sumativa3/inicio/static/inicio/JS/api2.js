$(document).ready(function(){
    let llave = "live_ODgIKnB8BcLGy1QqPRJY0YwmuuCln9ZmKfuftkQyEH3AXvK8TWWBBVa6j1rRVykg";
    $.get('https://api.thecatapi.com/v1/images/search?api_key='+llave+'', function(datos){
        $('#img_api').append("<img id='img_animal' src="+datos[0].url+">");
    }, 'json');
});