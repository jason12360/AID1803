def myfun(a,b,c):
	print('a-->',a)
	print('b-->',b)
	print('c-->',c)
#位置传参
myfun(100,200,300)

#序列传参
s1 = [11,22,33]
myfun(*s1)#等同于 myfun(s1[0],s1[1],s1[2])

s2 = (1.1,2.2,3.3)
myfun(*s2)

s3 = 'ABC'
myfun(*s3)

#关键字传参：
myfun(a = 100,b = 200, c = 300)
myfun(c = 30,b = 20, a = 10)

d1 ={'a':33,'b':22,'c':55}
myfun(**d1)

#综合传参
myfun(100,*(200,300))

myfun(*[100,200],300)

# myfun(c = 333,b=222,111) 错误

myfun(100,**{'c':334,'b':500})
myfun(**{'c':222,'a':999},b=333)
