# encoding:utf-8
first = input('请输入第一行')
second = input('请输入第二行')
third = input('请输入第三行')
length = max(len(first),len(second),len(third))
a= '%'+str(length)+'s' + '\n'
print(a*3%(first,second,third))



print(first.center(length),second.center(length),third.center(length),sep='\n')

