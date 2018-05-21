#我想调用 menu.py 模块里的show_menu函数

from mypack.menu import show_menu #从mypack包里的menu模块中导入show_menu函数

show_menu()
from mypack.games import contra, supermario, tank
contra.play()
supermario.play()
tank.play()

