$(function(){
        const list = $('UL.my_list');

        $('#add_item').click(function(){
            $('<li>Item</li>').appendTo(list);
        })
        $('#remove_item').click(function(){
            $('UL.my_list li:last-child').remove();
        })
        $('DIV#clear_list').click(function () {
            $('UL.my_list li').remove();
          });
    })
