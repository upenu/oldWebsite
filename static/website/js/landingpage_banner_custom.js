$(document).ready(function(){
  var detectViewPort = function() {
    var viewPortWidth = $(window).width();
    $('#banner-wrapper').css("width","100%");
  };
  $(function(){ detectViewPort(); });
  $(window).resize(function () { detectViewPort(); });
});
