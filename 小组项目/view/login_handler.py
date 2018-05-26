from view_exception import *
from login_view import Login_View
from register_view import Register_View
from register_view import *
import tkinter.messagebox
def do_login(view):
	if not view.validate():
		view.initial_focus.focus_set()
		return
	username = view.e1.get()
	password = view.e2.get()
	#检测用户名
	try:
		islegal(username,password)
		view.withdraw()
		view.update_idletasks()	
	except UsrnameOrPasswdBlankException:
		tkinter.messagebox.showerror(
			'检测用户名',
			'用户名或密码不能为空')
	except UsrnameOrPasswdNotExistException:
		tkinter.messagebox.showerror(
			'检测用户名',
			'用户名或密码不存在')
def do_register(view):
	view.destroy()
	r = Register_View(view.parent)
	r.focus_set()	
def islegal(username,password):
	'''
	这个方法用来判断用户名是否符合规定
	初级阶段暂定规定为用户名和密码不为空
	'''
	#假设用户在数据库中
	exist_in_database = True
	if (not username) or (not password):
		raise UsrnameOrPasswdBlankException()
	elif not exist_in_database:
		raise UsrnameOrPasswdNotExistException()
	return 