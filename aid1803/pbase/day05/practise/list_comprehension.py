   # 输入一个数值作为开始的数，用begin绑定
   #  再输入一个结束的整数用end绑定
   #      将 开始至结束的数中，平方加1能被,7整除的数放入列表中
   #  请输入开始数：1
   #  请输入结束数：20
    
start = int(input('请输入开始数：'))
end =int(input('请输入结束数：'))
print([x for x in range (start,end+1) if (x**2+1)%5 == 0])