# 2.输入任意个数，输入负数结束，打印出这些数的最大值，最小值

L=[]
while 1 :
    n = int(input('请输入一个数'))
    if n < 0:
        break
    L += [n]
print('这些数中最大值为：%d，最小值为：%d'%(max(L),min(L)))   

