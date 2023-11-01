$(
    function(){
        const div = $('#toggle_header');
        div.click(function(){
            $('header').toggleClass('red green');
        })
    }
);
