from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.db.models import F,Q
# Create your views here.
def add_views(request):
	# 方式1
	Author.objects.all().delete()
	Author.objects.create(name = '朱自清',age = 65)
	# 方式2
	obj = Author(name = '老舍',age=68,email='laoshe@163.com')
	obj.save()
	# 方式3
	dic = {
			'name':'莫言',
			'age':59,
			'email':'nuoyan@163.com',
			}
	obj = Author(**dic)
	obj.save()
	#像Book表中插入数据
	# Book.objects.create(title='背影',publicate_date = '1990-9-11')
	# obj = Book(title='茶馆',publicate_date='1968-6-12')
	# obj.save()
	# dic = {
	# 	'title':'红高粱',
	# 	'publicate_date':'1990-12-2'

	# }
	# obj = Book(**dic)
	# obj.save()
	return HttpResponseRedirect('/03_aulist')

def query_views(request):
	if request.method == 'GET':
		auList = Author.objects.filter(isActive=True)
		return render(request,'author.html',locals())
	else:
		post = request.POST
		id = post['id']
		name = post['name']
		age = post['age']
		email = post['email']
		author = Author.objects.get(id=id)
		author.name = name
		author.age = age
		author.email = email
		author.save()
		return HttpResponseRedirect('/03_aulist')

def order_views_asc(request):
	auList = Author.objects.filter(isActive=True).order_by('age')
	return render(request,'author.html',locals())

def order_views_desc(request):
	auList = Author.objects.filter(isActive=True).order_by('-age')
	return render(request,'author.html',locals())

def update_views(request):
	auList = Author.objects.filter(isActive=True)
	auList.update(age = 45)
	return render(request,'author.html',locals())

def delete_views(request,id):
	au = Author.objects.get(id=id)
	au.isActive = False
	au.save()
	# auList = Author.objects.filter(isActive=True)
	# return render(request,'author.html',locals())
	return HttpResponseRedirect('/03_aulist')

def change_views(request,id):
	au = Author.objects.get(id=id)
	return render(request,'author_m.html',locals())

def upage_views(request):
	Author.objects.all().update(age = F('age')+10)
	return HttpResponseRedirect('/03_aulist')

def doQ_views(request):
	auList = Author.objects.filter(Q(id=6)|Q(age__gte=70))
	return render(request,'author.html',locals())

def raw_views(request):
	sql = 'select * from index_author where id >= 295'
	auList = Author.objects.raw(sql)
	return render(request,'author.html',locals())

def oto_views(request):
	# wife = Wife.objects.get(id=6)
	# author = wife.author
	author = Author.objects.get(id=305)
	wife = author.w
	return render(request,'03_oto.html',locals())

def mto_views(request):
	# book = Book.objects.get(id=3)
	# publisher = book.publisher
	publisher = Publisher.objects.get(id=2)
	books = publisher.book_set.all()
	return render(request,'04_otm.html',locals())

def mtm_views(request):
	author = Author.objects.get(id=304)
	books = author.book.all()
	book = Book.objects.get(id=1)
	authors = book.author_set.all()
	return render(request,'05_mtm.html',locals())

def mtm_p_views(request):
	author = Author.objects.get(name='老舍')
	publishers = author.publisher.all()
	publisher = Publisher.objects.get(name='北京大学出版社')
	authors = publisher.author_set.all()
	return render(request,'06_mtm.html',locals())