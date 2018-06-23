from django.http import HttpResponse
#编写视图处理函数,一个函数相当于一个视图

def run_views(request):
	#request只要封装的是请求的信息
	return HttpResponse('<button>这是我的第一个Django程序</button>')

def run1_views(request,num):
	return HttpResponse('传递的参数是:'+num)

def run2_views(request,num1,num2):
	return HttpResponse('传递的第一个参数是:'+num1+'\n传递的第一个参数是:'+num2)

def show_views(request,name,age):
	return HttpResponse('传递的第一个参数是:'+name+'\n传递的第一个参数是:'+age)