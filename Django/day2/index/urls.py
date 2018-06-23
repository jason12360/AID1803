from django.conf.urls import url
from .views import *

#当访问路径是http://localhost:8000/news/...
#则交给这个文件来处理
urlpatterns = [
	#匹配访问路径是index的话,则交给index_views去处理
	url(r'^$',index_views),
	url(r'^login/$',login_views)
]