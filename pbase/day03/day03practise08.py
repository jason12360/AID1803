 # 3.打印1-20的整数，每行打印五个，打印四行，如：
 #    1 2 3 4 5
 #    6 7 8 9 10
 #    ...
 #    提示if语句可以嵌入while中
i = 1
while i <= 20:
    print(i,end = " ")
    if i % 5 == 0:
        print()
    i += 1
    
