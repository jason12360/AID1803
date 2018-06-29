$(function(){
	var bl = $('#bl>a')
	bl.click(function(){
		var uphone = $('[name=uphone]').val();

		var upwd = $('[name=upwd]').val();
		if (uphone.length == 0 || upwd.length==0){
			window.alert('用户名或密码不能为空');
		}else{
			$('#Lform')[0].submit();
		}
	});
});