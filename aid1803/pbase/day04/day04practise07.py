 # 输入一个数字，打印1，n之间的寄数，不包含n
n = int(input('请输入一个数字: '))
for i in range(1, n):
    if i % 2 == 0:
        continue
    print(i,end = ' ')
print()
