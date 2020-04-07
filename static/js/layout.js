var Layout = function () {
    var isMobileDevice = function() {
        return  ((
            navigator.userAgent.match(/Android/i) ||
            navigator.userAgent.match(/BlackBerry/i) ||
            navigator.userAgent.match(/iPhone|iPad|iPod/i) ||
            navigator.userAgent.match(/Opera Mini/i) ||
            navigator.userAgent.match(/IEMobile/i)
        ) ? true : false);
    }

    var WindowWidth = $(window).width();
    var WindowHeight = $(window).height();

    // var handleParallax = function () {
    //     $(window).load(function(){
    //         if (isMobileDevice() === false) {
    //             $("#message-block").parallax("50%",0.4);
    //             $("#facts-block").parallax("50%",0.4);
    //         }
    //     });
    // }

    var handleScrolling = function () {
        $(".scroll").on("click", function(event) {
            event.preventDefault();//the default action of the event will not be triggered
            $("html, body").animate({scrollTop:($("#"+this.href.split("#")[1]).offset().top)}, 600);
        });
    }

    /* Smooth scrolling and smart navigation when user scrolls on one-page sites */
    // var handleNavItemCurrent = function () {
    //     $(".header-navigation").onePageNav({
    //         currentClass: "current",
    //         scrollThreshold: 0
    //     });
    // }

    var handleHeaderPosition = function () {
        var CurrentHeaderPosition = $(".hheader").offset().top;// current header's vertical position
        
        var headerFix = function(){
            var CurrentWindowPosition = $(window).scrollTop();// current vertical position
            if (CurrentWindowPosition > CurrentHeaderPosition) {
                $(".hheader").addClass("fixNav");
            } else {
                $(".hheader").removeClass("fixNav");
            }
        };

        headerFix();// call headerFix() when the page was loaded
        if (navigator.userAgent.match(/iPhone|iPad|iPod/i)) {
            $(window).bind("touchend touchcancel touchleave", function(e){
                headerFix();
            });
        } else {
            $(window).scroll(function() {
                headerFix();
            });
        }
    }

    var handleGo2Top = function () {       
        var Go2TopOperation = function(){
            var CurrentWindowPosition = $(window).scrollTop();// current vertical position
            if (CurrentWindowPosition > 300) {
                $(".go2top").show();
            } else {
                $(".go2top").hide();
            }
        };

        Go2TopOperation();// call headerFix() when the page was loaded
        if (navigator.userAgent.match(/iPhone|iPad|iPod/i)) {
            $(window).bind("touchend touchcancel touchleave", function(e){
                Go2TopOperation();
            });
        } else {
            $(window).scroll(function() {
                Go2TopOperation();
            });
        }
    }



    function handleCounter() {
        /*$('.counter').counterUp({
            delay: 10,
            time: 1000
        });*/
    }

    var handlePortfolioSorting = function () {
        /*$(".sorting-grid").mixitup();*/
    }

    var handleFancybox = function () {
        if (!jQuery.fancybox) {
            return;
        }
        $(".zoom").fancybox();
    }

    var handleMobiToggler = function () {
        $(".mobi-toggler").on("click", function(event) {
            event.preventDefault();//the default action of the event will not be triggered
            
            $(".header").toggleClass("menuOpened");
            $(".header").find(".header-navigation").toggle(300);            
        });

        function SlideUpMenu () {
            $(".header-navigation a").on("click", function(event) {
                if ($(window).width()<1024) {
                    event.preventDefault();//the default action of the event will not be triggered
                    $(".header-navigation").slideUp(100);
                    $(".header").removeClass("menuOpened");
                }
            });
            $(window).scroll(function() {
                if (($(window).width()>480)&&($(window).width()<1024)) {
                    $(".header-navigation").slideUp(100);
                    $(".header").removeClass("menuOpened");
                }
            });
        }
        SlideUpMenu();
        $(window).resize(function() {
            SlideUpMenu();
        });
    }

        
    function valignCenterMessageFunction () {
         MessageCurrentElemHeight = $(".message-block .valign-center-elem").height();

        $(".message-block .valign-center-elem").css("position", "absolute")
            .css ("top", "50%")
            .css ("margin-top", "-"+MessageCurrentElemHeight/2+"px")
            .css ("width", "100%")
            .css ("height", MessageCurrentElemHeight);
    }

    function valignCenterPortfolioFunction () {
         PortfolioCurrentElemHeight = $(".portfolio-block .valign-center-elem").height();

        $(".portfolio-block .valign-center-elem").css("position", "absolute")
            .css ("top", "50%")
            .css ("margin-top", "-"+PortfolioCurrentElemHeight/2+"px")
            .css ("width", "100%")
            .css ("height", PortfolioCurrentElemHeight);
    }

    var valignCenterMessage = function () {
        valignCenterMessageFunction();
        $(window).resize(function() {
            valignCenterMessageFunction();
        });
    }
    var valignCenterPortfolio = function () {
        valignCenterPortfolioFunction();
        $(window).resize(function() {
            valignCenterPortfolioFunction();
        });
    }



    return {
        init: function () {
            //handlePromoBlock();
            //handleParallax();
            handleScrolling();
            //handleNavItemCurrent();
            handleHeaderPosition();
            handleCounter();
            handleGo2Top();
            handlePortfolioSorting();
            handleFancybox();
            //handleMobiToggler();
            valignCenterMessage();
            valignCenterPortfolio();
        },
    };
}();