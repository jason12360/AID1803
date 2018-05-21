#此为相对导入，当前所在位置为mypack.games.contra
from ..menu import show_menu
def play():
    print('正在玩魂斗罗')

print('魂斗罗模块被加载！')

def gameover():
    print('游戏结束')
    show_menu()