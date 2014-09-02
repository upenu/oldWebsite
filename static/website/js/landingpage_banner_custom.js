$(document).ready(function(){
  var detectViewPort = function() {
    var viewPortWidth = $(window).width();
    if (viewPortWidth < 1200)
      $('#banner-wrapper').css("width","100%");
    else
      $('#banner-wrapper').css("width","1200px");
  };
  $(function(){ detectViewPort(); });
  $(window).resize(function () { detectViewPort(); });
});