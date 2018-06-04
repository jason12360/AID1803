def myfun1(a,b,*,c,d): #c为命名关键字形参
	print(a,b,c)

myfun1(1,2,c=3,d=4)
# myfun1(1,2,3)#错的
def myfun2(a,*args,b,c):#b，c为命名关键字形参
 print(a,b,c,args)

myfun2(1,b=2,c=3)
myfun2(1,2,3,4,5,b=3,c=4)
myfun2(11,c=44,b=33)