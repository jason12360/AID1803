import re

pattern = r'\s+'
#获取正则表达式
obj = re.compile(pattern)
#通过对象调用findall
l = obj.findall('abcdabcabab',6,9)
#通过哦模块内函数findall
l2 = re.findall(obj,'abcdabcabab')
#使用split匹配目标字符串进行切割
# pattern = r'\s+'
l3 = obj.split('hello word hello kitty  nihao china')
#使用sub替换目标字符串中的匹配内容
l4 = obj.sub('##','hello word hello kitty  nihao china',2)
#使用subn替换目标字符串中的匹配内容
l5 = obj.subn('##','hello word hello kitty  nihao china')
print(l5)

