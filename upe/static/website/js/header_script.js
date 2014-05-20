$(document).ready(function(){
    //Turns nav-elements white on hover
    $(".nav-left").hover(function() { 
        $(this).css("color", "white");
        $(this).css( 'cursor', 'pointer');
    },
    function() {
        $(this).css("color", "#C9C9C9");
    });
    //Change cursor to pointer on hover over icons
    $(".icons").hover(function() { 
        $(this).css( 'cursor', 'pointer');
    },
    function() {
    });

    $("#signin").hover(function() { 
        $(this).css( 'cursor', 'pointer');
    },
    function() {
    });
    //Turns UPE-elements white on hover
    $("#title").hover(function() { 
        $(this).css("color", "white");
        $(this).css( 'cursor', 'pointer');
    },
    function() {
        $(this).css("color", "#C9C9C9");
    });
    //Dropdown menu on hover
    $("#about").hover(function() { 
        $("#drop-about").fadeIn(80)
    },
    function() {
        $("#drop-about").css("display", "none");
    });

    $("#ss").hover(function() { 
        $("#drop-ss").fadeIn(80)
    },
    function() {
        $("#drop-ss").css("display", "none");
    });

    $("#ir").hover(function() { 
        $("#drop-ir").fadeIn(80)
    },
    function() {
        $("#drop-ir").css("display", "none");
    });

    $("#cal").hover(function() { 
        $("#drop-cal").fadeIn(80)
    },
    function() {
        $("#drop-cal").css("display", "none");
    });
    //Highlights background on dropdown options
    $(".drop-op").hover(function() { 
        $(this).css("color", "white");
        $(this).css("background", "#363636");
        $(this).css( 'cursor', 'pointer');
    },
    function() {
        $(this).css("color", "#C9C9C9");
        $(this).css("background", "#242424");
    });

    //Hover over icons will change it from grey to white    
    $("#fbi").hover(function() {
        $(this).attr('src', 'static/assets/images/icons/w_fb.png');
    },
    function() {
        $(this).attr('src', 'static/assets/images/icons/g_fb.png');
    });

    $("#rssi").hover(function() {
        $(this).attr('src', 'static/assets/images/icons/w_rss.png');
    },
    function() {
        $(this).attr('src', 'static/assets/images/icons/g_rss.png');
    });

    $("#twi").hover(function() {
        $(this).attr('src', 'static/assets/images/icons/w_tw.png');
    },
    function() {
        $(this).attr('src', 'static/assets/images/icons/g_tw.png');
    });

    //toggles modal overlay and modal box 
    $('#signin').click(function(){
        $('#modal-overlay').fadeIn().css({'display': 'block'});
        $('#modal-container').fadeIn().css({'display': 'block'});
    });

    //cancel and submit buttons cause overlay and modal to disappear
    $('.button').click(function(){
        $('#modal-container').fadeOut();
        $('#modal-overlay').fadeOut();
    });
    //clicking on overlay causes modal box to go away
    $('#modal-overlay').click(function(){
        $('#modal-overlay').css({'display': 'none'});
        $('#modal-container').fadeOut();
    });

    //expanding search bar when search icon is clicked
    $('#searchi').click(function(){  
        $('#search-box-h').css({'display': 'block'});
        $('#search-box-h').fadeIn(500).animate({'width': '160'}, 330);
        $('#search-box-h').focus();
    });

    //collapsing search bar when something else is clicked
    $('#search-box-h').blur(function() {
        $('#search-box-h').css({'width': '0'});
        $('#search-box-h').css({'transition': 'width 0.5s ease-out'});
    })
});