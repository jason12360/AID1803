


f = open('myflush.txt','w')

f.write('我是第一行数据')
f.flush()
s = input('暂停中...')
f.write('我是第二行数据')
f.close()




