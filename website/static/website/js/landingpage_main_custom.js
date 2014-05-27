$(document).ready(function(){

  /* Pre-load first event. */
  $(".events-list-description").append($(".events-list-item").children("[class='description']").html());
  
  /* Toggle events. */
  $(".events-list-item").click(function() {
    $(".events-list-description").fadeOut(0);
    $(".events-list-description").empty();
    $(".events-list-description").append($(this).children("[class='description']").html());
    $(".events-list-description").fadeIn(500);
  });
});