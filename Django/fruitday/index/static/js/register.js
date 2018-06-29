$(function() {
    var bl = $('#bl>a');
    bl.text('注册');
    bl.click(function(){
        $('#Rform')[0].submit();
    });
    var br = $('#br>a');
    br.text('会员登录');
    br.attr('href', '/login/');

});