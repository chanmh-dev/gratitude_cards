window.onload = function() {
    var viewHeight = window.innerHeight;

    var slider1 = document.querySelector(".marquee1");
    var slider2 = document.querySelector(".marquee2");
    var slider3 = document.querySelector(".marquee3");

    var time1 = (slider1.offsetHeight * 2.0 + viewHeight * 2) / 300.0; 
    var time2 = (slider2.offsetHeight * 2.0 + viewHeight * 2) / 300.0; 
    var time3 = (slider3.offsetHeight * 2.0 + viewHeight * 2) / 300.0; 
    
    slider1.style.animationDuration = time1 + "s";
    slider2.style.animationDuration = time2 + "s";
    slider3.style.animationDuration = time3 + "s";
    
    }