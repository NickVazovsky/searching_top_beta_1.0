

$(function () {
  $('.example-popover').popover({
    container: 'body'
  })
    .on("mouseenter", function () {
    var _this = this;
    $(this).popover("show");
    $(".popover").on("mouseleave", function () {
        $(_this).popover('hide');
    });

})
    .on("mouseleave", function () {
    var _this = this;
    setTimeout(function () {
        if (!$(".popover:hover").length) {
            $(_this).popover("hide")
        }
    }, 100);
})
});
 /*.on("mouseleave", function () {
    var _this = this;
    setTimeout(function () {
        if (!$(".popover:hover").length) {
            $(_this).popover("hide")
        }
    }, 100);
});*/

//preloader
$(window).on('load', function () {
    var $preloader = $('.back-load'),
        $spinner   = $preloader.find('.box');
    $spinner.fadeOut();
    $preloader.delay(350).fadeOut('slow');
});


$(document).ready(function() {
    $('.analiz').on('click', function () {
        $('.change').show();
    });
});

$(document).mouseup(function (e) {
    var elem = $('.change');
    if(e.target!=elem[0]&&!elem.has(e.target).length){
        elem.hide();
    }
});


$(document).ready(function(){
    $('#all-pars').on('click',function() {
        $('.optim-block').hide(function () {
            $('.final-score').show();
            $(".all-tab").addClass('active');
            $(".opt-tab").removeClass('active');
            $(".index-tab").removeClass('active');
        });
    });
    $('#index-pars').on('click',function() {
        $('.optim-block').hide(function () {
            $('.final-score').hide();
            $('.index-block').show();
            $(".index-tab").addClass('active');
            $(".opt-tab").removeClass('active');
            $(".all-tab").removeClass('active');
        });
    });
    $('#opt-pars').on('click',function() {
        $('.index-block').hide(function () {
            $('.optim-block').show();
            $('.final-score').hide();
            $(".opt-tab").addClass('active');
            $(".index-tab").removeClass('active');
            $(".all-tab").removeClass('active');
        });
    });

    //close download form
     $('#download-list').on('click',function() {
        $('.down-list-varius').show( function(){
            $('.close-export').on('click', function(){
                 $('.down-list-varius').hide();
            });
        });
    });



















    // $('.action-index').on('click',function() {
    //     $('.optimiz').hide(function () {
    //         $('.index').show();
    //         $(".action-index").addClass('active-tab');
    //         $(".action-opt").removeClass('active-tab');
    //     });
    // });
    // $('.action-opt').on('click',function() {
    //     $('.index').hide(function () {
    //         $('.optimiz').show();
    //         $(".action-opt").addClass('active-tab');
    //         $(".action-index").removeClass('active-tab');
    //     });
    // });


    $('.action-go').on('click',function() {
        $('.yandex').hide(function () {
            $('.google').show();
            $(".action-go").addClass('active');
            $(".action-ya").removeClass('active');
        });
    });
    $('.action-ya').on('click',function() {
        $('.google').hide(function () {
            $('.yandex').show();
            $(".action-ya").addClass('active');
            $(".action-go").removeClass('active');
        });
    });


    $('.map-form').on('click', function () {
        $('.form-map').show();
    })
});


$(document).mouseup(function (e) {
    var elem = $('.form-map');
    if(e.target!=elem[0]&&!elem.has(e.target).length){
        elem.hide();
    }
});

//result ruk seo



//result ruk seo
// $(document).ready(function() {
//     $('.yaruk-js').on('click', function () {
//         $('.ruk-go').hide(function () {
//             $('.ruk-ya').show();
//         });
//     });
//     $('.goruk-js').on('click', function () {
//         $('.ruk-ya').hide(function () {
//             $('.ruk-go').show();
//         });
//     });
//     $('.smmruk-js').on('click', function () {
//         $('.ruk-go').hide();
//         $('.ruk-ya').hide(function () {
//             $('.ruk-smm').show();
//         });
//     });

// });


// $(document).ready(function() {
//     $('.tkd-js').on('click', function () {
//         $('.ruk-untext').hide();
//         $('.ruk-link').hide();
//         $('.ruk-header').hide(function () {
//             $('.ruk-tkd').show();
//         });
//     });
//     $('.header-js').on('click', function () {
//         $('.ruk-untext').hide();
//         $('.ruk-link').hide();
//         $('.ruk-tkd').hide(function () {
//             $('.ruk-header').show();
//         });
//     });
//     $('.untext-js').on('click', function () {
//         $('.ruk-link').hide();
//         $('.ruk-header').hide();
//         $('.ruk-tkd').hide(function () {
//             $('.ruk-untext').show();
//         });
//     });
//     $('.erlink-js').on('click', function () {
//         $('.ruk-header').hide();
//         $('.ruk-untext').hide();
//         $('.ruk-tkd').hide(function () {
//             $('.ruk-link').show();
//         });
//     });
// });



            $(".index-tab").addClass('active');
