# 练习：
#     写一个程序，让用户输入很多个正整数，当输入小于零的数时结束输入
#     1）输出这些数的和
#     2）输出这些数的最大的数和第二大的数
#     3）删除最小的数
#     4）按原来输入的顺序打印出剩余的这些数
l = []
while 1:
    n = int(input('请输入数字，输入小于“0”的数结束： '))
    if n < 0:
        break
    l.append(n)
l2 = l.copy()
l2.remove(max(l))
l.remove(min(l))
print('这些数的和为%d'%sum(l))
print('最大的数为%d，第二大的数为%d'%(max(l),max(l2)))
print('剩余的数为 :')
for a in l:
    print(a,end = ' ')