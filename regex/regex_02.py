import re

#compile对象的属性
reg = re.compile(r'(?P<tiger>(?P<dog>ab)cd(?P<cat>ef))')
print('flags:',reg.flags)#标识位常量
print('pattern:',reg.pattern)#正则表达式
print('groupindex:',reg.groupindex)#捕获组字典
print('groups:',reg.groups)#子组个数
#match对象的属性和方法
match_obj = reg.search('abcdefghig')
print('pos:',match_obj.pos)#目标字符串开头位置
print('endpos:',match_obj.endpos)#目标字符串结束位置
print('re:',match_obj.re)#正则表达式对象
print('string:',match_obj.string)#目标字符串
print('lastgroup:',match_obj.lastgroup)#最后一组的名字
print('lastindex:',match_obj.lastindex)#最后一组是第几组
print(match_obj.start())#匹配到的内容的开始位置
print(match_obj.end())#匹配到内容的结束位置
print(match_obj.span())#匹配的内容的起止位置
for i in range(4):
	print(match_obj.group(i))
print(match_obj.groups())
print(match_obj.groupdict())

