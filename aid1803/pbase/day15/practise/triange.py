# 2.写程序打印杨辉三角（只打印6层）
#          1   
#         1 1   
#        1 2 1  
#       1 3 3 1
#      1 4 6 4 1
#     1 5 10 10 5 1
# n = 6
# list = [[0 for x in range(2*n + 1)]for y in range(n)]
# list[0][n] = 1
# for i in range(1,n):
#     for j in range(2*n + 1):
#         if j-1 >=0 and j+1 <= 2*n:
#             list[i][j] = list[i-1][j-1] + list[i-1][j+1]

# for a in list:
#     for b in a:
#         if b == 0:
#             print(' ',end = '')
#         else:
#             print(b,end = '')
#     print()

def trian(n):
    b = [1]
    while n > 0:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b) - 1)] + [1]
        n -= 1

def main():
    n = int(input('请输入要打印的层数：'))
    for t in trian(n):
        print(' ' * (n-len(t)),end = '')
        for number in t:
            print(number,end = ' ')
        print()

main()