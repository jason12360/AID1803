from django import forms
from .models import *

class LoginForm(forms.ModelForm):
	class Meta:
			model=Users
			fields=['uphone','upwd']
			labels = {
				'uphone':'手机号',
				'upwd':'密码',
			}
			widgets={
				'uphone':forms.TextInput(
					attrs={
						'class':'entry',
					}
					),
				'upwd':forms.PasswordInput(
					attrs={
						'class':'entry',
					}),
			}