# 练习: 
#     1.输入一个圆的半径，打印出这个圆的面积
#     2.输入一个圆的面积，打印出这个圆的半径
#     面积 = pi × 半径的平方

import math



r = float(input('请输入一个圆的半径'))
print('这个圆的面积是%.2f'%(math.pi * math.pow(r,2)))
s = float(input('请输入一个圆的面积'))
print('这个圆的半径是%.2f'%(math.sqrt(s/math.pi)))