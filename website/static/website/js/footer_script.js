$(document).ready(function(){
  $("#icons1").hover(function() { 
    $(this).attr("src", "static/assets/images/icons/rss3.png");
    $(this).css( 'cursor', 'pointer');
  },
  function() {
    $(this).attr("src", "static/assets/images/icons/rss2.png");
  });
  $("#icons2").hover(function() { 
    $(this).attr("src", "static/assets/images/icons/twitter2.png");
    $(this).css( 'cursor', 'pointer');
  },
  function() {
    $(this).attr("src", "static/assets/images/icons/twitter.png");
  });
  $("#icons3").hover(function() { 
    $(this).attr("src", "static/assets/images/icons/fb2.png");
    $(this).css( 'cursor', 'pointer');
  },
  function() {
    $(this).attr("src", "static/assets/images/icons/fb.png");
  });
});