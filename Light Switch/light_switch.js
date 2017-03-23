'use strict';

// makes document ready
$(document).ready(function(){

    $('#btn').on('click', function(evt){
        // if the button has been clicked...
        if ($(this).hasClass("clicked")){
            // remove the class of being clicked
            $(this).removeClass('clicked');
            // switches to off image
            $('img').attr('src', 'off_720.jpg')
            
        } else {
            // allows button to be clicked
            $(this).addClass('clicked');
            //switch to on image
            $('img').attr('src', 'on_360.jpg')
        }
    });
});