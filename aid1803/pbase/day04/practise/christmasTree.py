
# 2.输入一个整数（代表树干的高度）
#     打印如下一颗圣诞树
# 输入2
#     ×
#    ×××
#     ×
#     ×
# 输入3
#     ×
#    ×××
#   ×××××
#     ×
#     ×
#     ×
n = int(input('请输入树的高度'))
for i in range(n):
    print(('*' * (1+ i*2)).center(1+n*2))
for i in range(n):
    print('*'.center(1+n*2))
