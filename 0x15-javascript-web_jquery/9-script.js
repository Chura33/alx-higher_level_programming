$(function(){
        $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data, statsCode)=>{
            $('DIV#hello').text(`${data.hello}`);
        })
    });
