# def show_table():
#     L = [str(y) + 'x' + str(x) + '='+ str(x*y) for x in range(1,10) for y in range(1,x+1)]
#     pointer = 0
#     for i in range(1,10):
#         print(' '.join(L[pointer:pointer + i]))
#         pointer += i

def show_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(str(i) + 'x' + str(j) + '=' + str(i*j),end =' ')
        print()


show_table()


