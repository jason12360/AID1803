from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name','age','email')
	list_display_links=('name','email',)
	list_editable = ('age',)
	search_fields = ('name','book','publisher')
	list_filter = ('book','publisher')
	# fields = ('email',('name','age'))
	fieldsets = (
				#分组1
					(
						'基本信息',{
									'fields':('name','email')
									}
					),
				#分组2
					(
						'可选信息',{
									'fields':('age','isActive','book','publisher'),
									'classes':('collapse','extrapretty'),
									}
					)
				)
admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publicate_date','publisher')
	date_hierarchy = 'publicate_date'
	list_filter = ['publisher']
	search_fields = ['publisher','title']
admin.site.register(Book,BookAdmin)

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name','address','city','website')
	list_editable = ('address','city')
	list_filter = ('address','city')
	fieldsets = (

					(
						'基本选项',{
							'fields':('name','address','city')
						}
					),
					(
						'可选选项',{
							'fields':('country','website'),
							'classes':('collapse',),

						}
					)
				)

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)