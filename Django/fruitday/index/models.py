from django.db import models
# 	练习:
# 		完善 FruitDay中的部分Models
# 			1.Models:商品类型,商品,用户
# 			2.商品类型 - GoodType
# 				1.类型名称 - title 
# 				2.类型的图片 - picture 默认上传至static/upload/goodstype
# 				3.类型的描述 - desc 200chars
# 			3.商品 - Goods
# 				1.商品名称 - title
# 				2.商品价格 - price(DecimalField)
# 				3.商品规格 - spec
# 				3.商品图片 - picture 默认上传至static/upload/goods
# 				4.销售状态 - isActive(默认值为True)
			# 4.用户 - Users
			# 	1.用户名 - uname
			# 	2.密码 - upwd
			# 	3.手机号 - uphone
			# 	4.邮箱 - uemail
			# 	5.状态 - isActive
# # Create your models here.

class GoodType(models.Model):
	title = models.CharField(max_length=30,verbose_name='类型名称')
	picture = models.ImageField(upload_to='static/upload/goodstype',verbose_name='类型图片')
	desc = models.CharField(max_length=100,verbose_name='类型描述')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='商品类型'
		verbose_name_plural='商品类型'



class Goods(models.Model):
	title = models.CharField(max_length=30,verbose_name='商品名称')
	picture = models.ImageField(upload_to='static/upload/goods',verbose_name='商品图片')
	price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='商品价格')
	spec = models.CharField(max_length=50,verbose_name='商品规格')
	isActive = models.BooleanField(default=True,verbose_name='是否激活')
	good_type = models.ForeignKey('GoodType',on_delete = models.CASCADE,null=True,verbose_name='商品类型')
	def __str__(self):
		return self.title

	class Meta:
		verbose_name='商品'
		verbose_name_plural='商品'

class Users(models.Model):
	uname = models.CharField(max_length=30)
	upwd = models.CharField(max_length=100)
	uphone = models.CharField(max_length=11)
	uemail = models.EmailField(null=True)
	isActive = models.BooleanField(default=True)


