# 3.已知有列表：
#     L = [[3,5,8],10,[[13,14],15],18]
#     1)写一个函数 print_list(lst) 打印出列表中所有数字
#     2）打印出列表中所有元素的和
L = [[3,5,8],10,[[13,14],15],18]
def print_list(l):
    for i in l:
        if type(i) is list:
            print_list(i)
        else:
            print(i)

def print_sum(l):
    sum = 0
    for i in l:
        if type(i) is list:
            sum += print_sum(i)
        else:
            sum += i
    return sum

print_list(L)
print('和为：',print_sum(L)) 