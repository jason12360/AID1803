# 输入一个数打印指定宽度的正方形
#     输入5
#     打印如下图形
#     1 2 3 4 5
#     2 3 4 5 6
#     3 4 5 6 7
#     4 5 6 7 8
#     5 6 7 8 9 

n = int(input('请输入正方形的宽度'))
# i = 1
# j = 0
# while j < n  :
#     i = 1
#     while i <= n:
#         print(i+j,end = " ")
#         i += 1
#     print()
#     j += 1

for i in range(1,n + 1):
    for  j in range(i,i + n):
        print(j,end = ' ')
    print()

    
