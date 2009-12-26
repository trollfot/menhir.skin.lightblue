$(document).ready(function(){
    $("dl.additional-actions").hover(
        function() {
           $("dd", this).slideDown('fast');
           $(this).addClass("unfolding");
        }, 
        function() {
           $("dd", this).slideUp('fast');
           $(this).removeClass("unfolding");
        } 
    );
});
