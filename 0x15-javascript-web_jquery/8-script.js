$(function()
    {
        $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, textStatus){
            for (let i=0; i < data.results.length; i++){
                $('UL#list_movies').append(`<li>${data.results[i].title}</li>`);
            }
        })
    });
