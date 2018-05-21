# 任意输入一些英文词，每次输入一个，当输入0时，结束
#     打印输入的单词的个数（去重），打印到单词的终端
#     如：
#         ABC
#         abc
#         ABCD
#         abc
#         单词个数：3
#         单词如下：
#         abc
#         ABC
#         ABCD

S = set()
while 1:
    a = input('请输入一些英文单词(输入“0”结束): ')
    if a == '0':
        break
    S.add(a)
print('单词个数: ',len(S))
print('单词如下: ')
for s in S:
    print(s)