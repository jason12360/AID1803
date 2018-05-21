def list_input():
    L =[]
    while True:
        s = input('请输入字符串：')
        if not s:
            return L
        else:
            L.append(s+'\n')

def save_input(l,filename = 'input.txt'):    
    file = open(filename,'w')
    file.writelines(l)
    file.close()

def read_input(filename = 'input.txt'):
    
    file = open(filename)
    lines = file.readlines()
    for n,l in enumerate(lines,1):
        print('第%d行：%s'%(n,l.rstrip('\n')))
    file.close()

def main1():
    try:
        input_list = list_input()
        save_input(input_list)
    except IOError:
        pass

def main2():
    try:
        read_input()
    except IOError:
        pass

main2()

