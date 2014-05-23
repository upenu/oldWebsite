$(function() {
  var Page = (function() {
    var $nav = $( '#nav-dots > span' ),
      slitslider = $( '#slider' ).slitslider( {
        onBeforeChange : function( slide, pos ) {
          $nav.removeClass( 'nav-dot-current' );
          $nav.eq( pos ).addClass( 'nav-dot-current' );
        }
      }),

      init = function() {
        initEvents();
      },
      initEvents = function() {
        $nav.each( function( i ) {
          $( this ).on( 'click', function( event ) {
            var $dot = $( this );
            if( !slitslider.isActive() ) {
              $nav.removeClass( 'nav-dot-current' );
              $dot.addClass( 'nav-dot-current' );
            }
            slitslider.jump( i + 1 );
            return false;
          });
        });

      },
      switchSlides = function(slideNum) {
        console.log(slideNum);

        slitslider.jump( slideNum );
      };
      return { init : init, switchSlides: switchSlides };
  })();

  Page.init();
  $(".sl-slider").addClass( 'sl-trans-elems' );
  var counter = 1;
  var NUMSLIDES = 3; // Change to number of slides
  window.setInterval(function(){
    $(".sl-slider").removeClass( 'sl-trans-elems' );
    Page.switchSlides(counter % NUMSLIDES+1);
    counter += 1;
    }, 7000);
});