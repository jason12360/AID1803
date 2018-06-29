from django import forms
from .models import *
#为topic下拉列表初始化一组数据-元组
TOPIC_CHOICE=(
	('level1','好评'),#=<option value='level1'>好评</option>	
	('level2','中评'),
	('level3','差评'),
)
class RemarkForm(forms.Form):
	#创建一个subject属性,表示评论标题,显示成文本框
	#label属性表示生成的控件前面的提示文本
	#initial表示初始化的数据,等同于控件的value属性
	subject = forms.CharField(label='标题',initial='初始数据')
	#创建一个email属性,表示邮箱,显示成email控件
	email = forms.EmailField(label='邮箱')
	#创建一个message属性,表示评论内容,显示成多行文本域
	message = forms.CharField(label='内容',widget=forms.Textarea)
	#创建一个topic属性,表示评论级别,显示成一个下拉列表
	topic = forms.ChoiceField(label='评价',choices = TOPIC_CHOICE)
	#创建一个isSave属性,表示是否保存,显示成复选框
	isSave = forms.BooleanField(label='是否保存')

class RegisterForm(forms.Form):
	uname = forms.CharField(label='用户名',widget = forms.TextInput(
							attrs={
								'placeholder' : '请输入用户名',
								'class':'form-control',
							}
							))
	upwd = forms.CharField(label='密码',widget=forms.PasswordInput(
							attrs = {
								'placeholder':'请输入密码',
								'class':'form-control',
							}))
	uemail = forms.CharField(label='邮箱',widget=forms.EmailInput(
							attrs ={
								'placeholder':'请输入邮箱'
							}
							))
	uage = forms.CharField(label='年龄',widget=forms.NumberInput(
							attrs={
								'placeholder':'请输入年龄'
							}))

class LoginForm(forms.ModelForm):
	#创建内部类meta
	class Meta:
		#1.指定关联的models是谁
		model = Users
		#2.生成控件的属性们
		# fields = '__all__'
		fields = ['uname','upwd']
		#3.每个控件对应的label
		labels = {
				'uname':'用户名',
				'upwd':'密码',
		}
		widgets={
			'uname':forms.TextInput(attrs={'placeholder':'请输入用户名'}),
			'upwd':forms.PasswordInput(attrs={'placeholder':'请输入密码'}),
		}

# class RegisterForm(forms.ModelForm):
# 	class Meta:
# 		model = Users
# 		fields = "__all__"
# 		labels = {
# 			'uname':'用户名称',
# 			'upwd':'用户密码',
# 			'uemail':'用户邮箱',
# 			'uage':'用户年龄',
# 		}