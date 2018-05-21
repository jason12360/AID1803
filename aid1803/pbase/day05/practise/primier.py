# 1.输入一个整数n代表结束的数
#     将1-n之间所有的素数计算出来并存入到列表L中
#         1）最后打印此列表中的全部素数
#         2）打印这些素数的和

n = int(input('请输入一个正整数：'))
L= []
for x in range(1,n+1):
    for y in range(2,x):
        if x % y ==0:
            break
    else:
        L.append(x)
print(L)
print(sum(L))