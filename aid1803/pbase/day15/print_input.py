def print_input(input_list):
    for k,n in enumerate(input_list,1):
        print('第%d行：%s'%(k,n))


L = []
while True:
    user_input = input('请输入：')
    if user_input:
        L.append(user_input)
    else:
        break
print_input(L)
