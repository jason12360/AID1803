l = []
while 1:
    s = input('请输入一行文字： ')
    if s != '':
       l = [s] + l
    else:
        break
print(l)
