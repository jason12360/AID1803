from django.conf.urls import url
from .views import *

#当访问路径是http://localhost:8000/news/...
#则交给这个文件来处理
urlpatterns = [
	#匹配访问路径是index的话,则交给index_views去处理
	url(r'^index/$',index_views),
	url(r'^01_template/$',template_views),
	url(r'^02_render/$',render_views),
	url(r'^03_variable/$',var1_views),
	url(r'^04_variable/$',var2_views),
	url(r'^05_exer/$',exer_views),
	url(r'^06_tag/$',tag_views),
    url(r'^07_static/$',static_views),
    url(r'^08_parent/$', parent_views),
    url(r'^09_child/$', child_views,name='child'),
    url(r'^10_name/$', name_views),
    url(r'^11_arg/(\d{4})/(\d{2})/$', arg_views,name='args'),

]