a = int(input('请输入这个矩形的宽度'))
# shape= '*'*a + '\n' \
# + '*' + ' '*(a-2) + '*' + '\n'\
# + '*' + ' '*(a-2) + '*' + '\n'\
# + '*'*a 
# print(shape);

first = '*'*a
second = '*' + ' '*(a-2) + '*'
print(first,second,second,first,sep = '\n')