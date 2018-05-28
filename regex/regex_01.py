import re

l1 = re.finditer(r'\d+','2008年是个多事之秋,512地震，08奥运等')
print(l1)
for i in l1:
	print(i.group())
l2 = re.match(r'foo','foo,food on the table')
l2 = re.search(r'foo','Foo,food on the table')
try:
	obj = re.fullmatch('\w+','abcd e123')
	print(obj.group())
except AttributeError as e:
	print(e)

	