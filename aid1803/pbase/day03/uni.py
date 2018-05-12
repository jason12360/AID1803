# 写一个程序，输入一段字符串，如果字符串不为空，则把第一个字符的UNICODE编码值打印出来
s = input('请输入一段字符串')
if s =='':
    print('输入不能为空')
else:
    print('您输入的字符串的第一个字符的UNICODE为',ord(s[0]))