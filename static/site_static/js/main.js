$(function(){
    'use-strict';
    // Adjusts Slider height
    var winH = $(window).height(),
        navH = $('.navbar').innerHeight();
    $('.carousel-item img').height(winH-navH);
 


});

window.onscroll = function () {fixedFunc()}

var navbar = document.getElementById("main-navbar"),
    sticky = navbar.offsetTop;

function fixedFunc(){

    if (window.pageYOffset >= sticky){
        navbar.classList.add("fixed-top");
    } else {
        navbar.classList.remove("fixed-top");
    }
}

$(function () {
    $('.material-tooltip-main').tooltip({
      template: '<div class="tooltip md-tooltip"><div class="tooltip-arrow md-arrow"></div><div class="tooltip-inner md-inner"></div></div>'
    });
  })
