$(function () {
	$('#frmLogin').submit(function(){
		var uname = $('[name=uname]').val();
		var upwd = $('[name=upasswd]').val();
		if (uname.length==0||upwd.length==0){
			return false;
		}
		return true;
	});
});