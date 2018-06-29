
from django.conf.urls import url,include
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^01_add/$',add_views),
	url(r'^02_query/$',query_views),
	url(r'^02_query/order_by_age_asc$',order_views_asc),
	url(r'^02_query/order_by_age_desc$',order_views_desc),
	url(r'^03_aulist/$',query_views),
	url(r'^04_update/$',update_views),
	url(r'^05_delete/(\d+)/$',delete_views,name='del'),
	url(r'^06_au/(\d+)/$',change_views,name='mod'),
	url(r'^07_upage/$',upage_views),
	url(r'^08_doQ/$',doQ_views),
	url(r'^09_raw/$',raw_views),
	url(r'^10_oto/$',oto_views),
	url(r'^11_mto/$',mto_views),
	url(r'^12_mtm/$',mtm_views),
	url(r'^13_mtm/$',mtm_p_views),
]