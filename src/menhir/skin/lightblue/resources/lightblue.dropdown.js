$(document).ready(function(){
    $(".incontext-action").hover(
        function() {
           $("dd", this).show();
           $(this).addClass("unfolding");
        }, 
        function() {
           $("dd", this).hide();
           $(this).removeClass("unfolding");
        } 
    );
});
