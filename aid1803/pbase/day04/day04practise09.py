#    输入三行文字，将这三行文字保存于一个列表L中，并打印
#     再打印列表中字符串所有字符的个数
# 如：
#     请输入：a b c回车
#     请输入：1 2 3 4 回车
#     生成如下列表：
#     print（L）, ['abc','1234']
#     总字符数：7

l1 = input('请输入第一行文字')
l2 = input('请输入第二行文字')
l3 = input('请输入第三行文字')
L=[l1,l2,l3]

sum = len(l1) + len(l2) +len(l3)
print(L)
print('总字符数： ',sum)