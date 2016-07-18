$(document).ready(function() {
    $('.call-to-action').click(function(){
        $(this).addClass('active');
       $('html, body').animate({scrollTop:$('#content').position().top - 60}, 3000);
    });
});
