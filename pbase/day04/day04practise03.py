s = input('请输入任意字符串')
count_a = 0
count_space = 0
# for ch in s:
#     if ch == 'a':
#         count_a += 1
#     if ch == ' ':
#         count_space += 1
# print('你输入的字符串中，“a”有%d个，“空格”有%d个'%(count_a,count_space))

i = 0

while i < len(s):
    if s[i] == 'a':
        count_a += 1
    if s[i] == ' ':
        count_space += 1
    i += 1

print('你输入的字符串中，“a”有%d个，“空格”有%d个'%(count_a,count_space))
     