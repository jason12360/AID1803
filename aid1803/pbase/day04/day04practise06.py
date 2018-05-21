 # 已知有字符串'ABC'和字符串'123'，用以上两个字符串生成如下字符串'A1''A2''A3'....
s1 = 'ABC'
s2 = '123'
for i in s1:
    for j in s2:
        print(i+j)
