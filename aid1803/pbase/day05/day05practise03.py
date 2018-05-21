 # 输入一段字符串，打印出这个字符串中出现过的字符以及此字符出现的个数
#     如：
#         请输入：abcdaba
#         打印结果如下：
#         a:3次
#         b:2次
#         c:1次
#         d:1次
#         abcd顺序不强求
s = input('请输入: ')
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for k in d:
    print(k,':',d[k],'次')