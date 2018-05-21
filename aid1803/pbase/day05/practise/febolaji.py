 # 3.计算20个斐波那契数存于列表当中，打印这20个数 1,1,2,3,5,8
L=[1,1]
for i in range(2,20):
    L.append(L[i-2] + L[i-1])
print(L)