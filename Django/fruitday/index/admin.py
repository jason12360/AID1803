from django.contrib import admin
from .models import *
# Register your models here.
class GoodTypesAdmin(admin.ModelAdmin):
	list_display = ['title','picture','desc']
	search_fields = ['title']
admin.site.register(GoodType,GoodTypesAdmin)
class GoodsAdmin(admin.ModelAdmin):
	list_display = ['title','picture','price','spec','good_type','isActive']
	list_editable = ['isActive']
	search_fields=['title','good_type']
	list_filter=['good_type']
	fieldsets = (
				('商品名称',{
					'fields':('title',)
				}),
				('商品信息',{
					'fields':('picture','price','spec','good_type','isActive')
				})

				
				)
admin.site.register(Goods,GoodsAdmin)

admin.site.register(Users)