 # 写一个程序
 #    输入一个开始整数用变量begin绑定
 #    输入一个结束整数用变量end绑定
 #    打印begin到end的每一个整数
begin = int(input('请输入开始的数'))
end = int(input('请输入结束的数'))
for i in range(begin,end):
    print(i,end = ' ')