$(function() {
    $.fakeLoader({
        spinner: "spinner2",
        bgColor: "#614cab"
    });
    $("a").on("click", function(a) {
        if (this.hash !== "") {
            a.preventDefault();
            var b = this.hash;
            $("html, body").animate({
                scrollTop: $(b).offset().top - 50
            }, 850)
        }
    });
    $(window).on("scroll", function() {
        var a = $(this).scrollTop();
        if (a > 50) {
            $(".navbar").addClass("navbar-fixed")
        } else {
            $(".navbar").removeClass("navbar-fixed")
        }
    });
    $(".filtr-container").imagesLoaded(function() {
        var a = $(".filtr-container").filterizr()
    });
    $(".portfolio-filter-menu li").on("click", function() {
        $(".portfolio-filter-menu li").removeClass("active");
        $(this).addClass("active")
    });
    $(".portfolio").each(function() {
        $(this).magnificPopup({
            delegate: ".portfolio-popup",
            type: "image",
            gallery: {
                enabled: true
            }
        })
    })
});