 # 1.从程序中输入一个数n
 #    计算 1+2+...+n
n= int(input('请输入一个数n'))
sum = 0
i = 1
while(i <= n):
    sum += i
    i += 1
print('结果为',sum)