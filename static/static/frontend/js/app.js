/* Theme Name: Quickgen - Multipurpose Templates
   Author: Shreethemes
   Version: 1.0.0
   Created: May 2019
   File Description:Main JS file of the template
*/

(function ($) {
    'use strict';

    // Magnific Popup
    $('.mfp-image').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        mainClass: 'mfp-fade',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1]
        }
    });

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    // Loader 
    $(window).on('load', function() {
        $('#status').fadeOut();
        $('#preloader').delay(350).fadeOut('slow');
        $('body').delay(350).css({
            'overflow': 'visible'
        });
    });

    // BACK TO TOP
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    }); 

    $(".back-to-top").on("click", function() {
        $("html, body").animate({ scrollTop: 0 }, 1000);
        return false;
    });

    $("#cart").on("click", function() {
        $(".shopping-cart").fadeToggle( "fast");
    });
})(jQuery) 