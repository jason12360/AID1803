# class Shape:
#     def draw(self):
#         pass
class Point():
    def draw(self):
        print('正在画一个点')

class Circle():
    def draw(self):
        print('正在画一个圆')

def my_draw(s):
    s.draw() #调用哪个方法呢，在运行时动态决定调用方法

s1 = Circle()
s2 = Point()
my_draw(s1)
my_draw(s2)
