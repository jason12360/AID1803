from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.

def request_views(request):
	scheme = request.scheme
	body = request.body
	host = request.get_host()
	path = request.path
	method = request.method
	get = request.GET
	post = request.POST
	cookies = request.COOKIES
	return render(request,'01_request.html',locals())

def login_views(request):
	if request.method == 'GET':
		return render(request,'02_login.html',locals())
	else:
		scheme = request.scheme
		body = request.body
		host = request.get_host()
		path = request.path
		method = request.method
		get = request.GET
		post = request.POST
		cookies = request.COOKIES
		uname = post['uname']
		upasswd = post['upasswd']
		return render(request,'01_request.html',locals())

def get_views(request):
	uname = request.GET.get('uname','')
	upasswd = request.GET.get('upasswd','')
	if uname and upasswd:
		return HttpResponse('用户名:'+uname+',密码'+upasswd)
	else:
		return render(request,'02_login1.html')

def query_views(request):
	id = request.GET.get('id','')
	name = request.GET.get('name','')
	return HttpResponse('id:'+id+',name'+name)

def form_views(request):
	if request.method == 'GET':
		form = RemarkForm()
		return render(request,'04_form.html',locals())
	else:
		form = RemarkForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			return render(request,'05_forminfo.html',locals())
		else:
			return HttpResponse('数据提交不符合规范')

def register_views(request):
	if request.method == 'GET':
		form = RegisterForm()
		return render(request,'06_register.html',locals())
	else:
		form = RegisterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			users = Users(**cd)
			users.save()
			return HttpResponse('Register OK')
		else:
			return HttpResponse('wrong')

def modelForm_views(request):
	if request.method =='GET':
		form = LoginForm()
		return render(request,'06_login.html',locals())

def addCookie_views(request):
	#不使用模板
	# resp = HttpResponse('添加cookies成功')
	# resp.set_cookie('uname1','zsf',60*60*24)
	# return resp

	#使用模板
	# resp = render(request,'07_setcookie.html',locals())
	# resp.set_cookie('uname2','zwj',60*60*24*31)
	# return resp

	#使用重定向
	resp = HttpResponseRedirect('/02_login/')
	resp.set_cookie('uname2','zcz',60*60*24*31)
	return resp

def getCookie_views(request):
	cookies = request.COOKIES
	print(cookies)
	return HttpResponse('get cookies OK')

def setSession_views(request):
	uname = 'sanfeng.zhang'
	uemail = 'sanfeng.zh@163.com'
	#将以上两个数据保存进session
	request.session['uname']=uname
	request.session['uemail'] = uemail
	return HttpResponse('Add Session Success!')

def getSession_views(request):
	uname = request.session.get('uname')
	uemail = request.session.get('uemail')
	return HttpResponse('uname:'+uname +',uemail'+uemail)