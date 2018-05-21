# 输入三段字符，使其打印如下：
# +--------------+
# | aaaaaaaaaaaa |
# |    aaaaa     |
# |      a       |
# +--------------+


a = input('请输入第一段字符: ')
b = input('请输入第二段字符: ')
c = input('请输入第三段字符: ')
length = max(len(a),len(b),len(c))

def centerWord(s,n):
    '''本函数用于是一个输入的字符串s在n个空格中居中'''
    frontspace = ((n-len(s)) // 2 ) * ' '
    backspace = (n - len(frontspace) - len(s) ) * ' '
    return frontspace + s + backspace

top_line = bottom_line = '+' + '-' * (length + 2) + '+'
first = '| ' + centerWord(a,length) + ' |'
second ='| ' + centerWord(b,length) + ' |'
third = '| ' + centerWord(c,length) + ' |'
print(top_line,first,second,third,bottom_line,sep = '\n')