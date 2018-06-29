from django.shortcuts import render,HttpResponse
from .models import *
from .forms import *
# Create your views here.
def login_views(request):
	form = LoginForm()
	if request.method =='GET':
		try:
			cookies = request.COOKIES
			uid = cookies.get('uid')
			uphone = cookies.get('uphone')
			user = Users.objects.filter(id=uid,uphone = uphone)
			uname = user[0].uname
			if user:
				return HttpResponse('欢迎回来'+uname)
			else:
				return render(request,'login.html',locals())
		except Exception as e:
			print(e)
			return render(request,'login.html',locals())
	else:
		uphone = request.POST.get('uphone')
		upwd = request.POST.get('upwd')
		try:
			user = Users.objects.get(uphone=uphone)
			if user.upwd == upwd:
				resp = HttpResponse('登陆成功')
				if 'remember' in request.POST:
					resp.set_cookie('uphone',uphone,60*60*24)
					resp.set_cookie('uid',user.id,60*60*24)
				return resp
			else:
				errMsg = '密码错误'
				return render(request,'login.html',locals())
		except Exception as e:
			print(e)
			errMsg = '手机号不存在'
			return render(request,'login.html',locals())
def register_views(request):
	if request.method == 'POST':
		uphone = request.POST.get('uphone','')
		upwd = request.POST.get('upwd','')
		uname = request.POST.get('uname','')
		uemail = request.POST.get('uemail','')
		uList = Users.objects.filter(uphone = uphone)
		if uList:
			errMsg = '手机号码已经注册'
			return render(request,'register.html',locals())
		else:
			user = Users(uname = uname,upwd = upwd,uphone=uphone,uemail=uemail)
			user.save()
			return HttpResponse('注册成功')
	else:
		form = LoginForm()
		return render(request,'register.html',locals())
