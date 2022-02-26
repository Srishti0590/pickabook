// window.addEventListener("scroll", function(){
//     var navbar = document.querySelector(".navbar");
//     navbar.classList.toggle("sticky", window.scrollY > 0);
// });

$(document).ready(function() {
    $(window).scroll(function(){
        if(this.scrollY > 500){
            $('.arrow').addClass("show");
        }else{
            $('.arrow').removeClass("show");
        }

    });

    $('.arrow').click(function(){
        $('html').animate({scrollTop:0})
    });

    $('#owl-demo').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        autoplayHoverPause:true,
        autoplay:true,
        autoplayTimeout:3000,

        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:4
            }
        }
    });
    $('#owl-demo1').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        autoplayHoverPause:true,
        autoplay:true,
        autoplayTimeout:3000,

        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:4
            }
        }
    });
    $('#owl-demo2').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        autoplayHoverPause:true,
        autoplay:true,
        autoplayTimeout:3000,

        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });
    $('#owl-demo3').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        autoplayHoverPause:true,
        autoplay:true,
        autoplayTimeout:3000,

        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });
    $('#owl-demo4').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        autoplayHoverPause:true,
        autoplay:true,
        autoplayTimeout:3000,

        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });
    $('#owl-demo5').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        autoplayHoverPause:true,
        autoplay:true,
        autoplayTimeout:3000,

        responsive:{
            0:{
                items:2
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });
});


$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY>50){
            $('.navbar').addClass("sticky");

        }else{
            $('.navbar').removeClass("sticky");
        }
    });



});

jQuery(function($) {

    // Function which adds the 'animated' class to any '.animatable' in view
    var doAnimations = function() {

      // Calc current offset and get all animatables
      var offset = $(window).scrollTop() + $(window).height(),
          $animatables = $('.animatable');

      // Unbind scroll handler if we have no animatables
      if ($animatables.length == 0) {
        $(window).off('scroll', doAnimations);
      }

      // Check all animatables and animate them if necessary
          $animatables.each(function(i) {
         var $animatable = $(this);
              if (($animatable.offset().top + $animatable.height() - 20) < offset) {
          $animatable.removeClass('animatable').addClass('animated');
              }
      });

      };

    // Hook doAnimations on scroll, and trigger a scroll
      $(window).on('scroll', doAnimations);
    $(window).trigger('scroll');

  });


$('#rating-form').on('change','[name="rating"]',function(){
	$('#selected-rating').text($('[name="rating"]:checked').val());
});
