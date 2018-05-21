# 3.任意输入一个数n代表三角形的高度，打印如下
#     1
#    121
#   12321
#  1234321

# 4.将第三题打印三角形变为打印菱形

n = int(input('请输入三角形的高度： '))
# for i in range(n*(2*n-1)):
#     m = i//(2*n-1)+1
#     l = i%(2*n-1)+1  
#     if m+l <= n:
#         print(' ',end = '')
#     elif  2*n + m - l <=n:
#         if l == 2*n-1:
#             print(' ')
#         else:
#             print(' ',end = '') 
#     else:
#         print(m - abs(l-n),end = '')


for i in range(n):
    print(' ' * (n-i-1),end = '')
    for j in range(1,i+2):
        print(j,end = '')
    for z in range(i,0,-1):
        print(z,end = '')
    print()
for a in range(n-2,-1,-1):
    print(' ' * (n-a-1),end = '')
    for j in range(1,a+2):
        print(j,end = '')
    for z in range(a,0,-1):
        print(z,end = '')
    print()



