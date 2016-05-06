$(function(){
    // Hide sections at start
    $('#infoSection').hide()
    $('#download_butt').hide()
    $('#reStart').hide()

    if ($('#settings_wrapper').text().length != 181){
        $('#beginForms').hide()
        $('#download_butt').show()
        $('#reStart').show()
    }

    $('#reStart').on('click', function(){
        window.location.assign('/')
    })

    // Hide and Show info page
    $('#info').on('click', function(){
        if ($('#infoSection').is(':hidden')){
            $('#infoSection').fadeToggle()
            $("html,body").animate({
                scrollTop: $('#infoSection').offset().top},
                'slow');
        } else {
            $("#infoSection").fadeToggle()
        }
    });

    $('#info2').on('click', function(){
        if ($('#infoSection').is(':hidden')){
            $('#infoSection').fadeToggle()
            $("html,body").animate({
                scrollTop: $('body').offset().top},
                'slow');
        } else {
            $("#infoSection").fadeToggle()
            $("html,body").animate({
                scrollTop: $('body').offset().top},
                'slow');
            }
        });

});
