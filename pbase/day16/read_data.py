# 练习：
#     将如下数据用文本编辑器sublime写入的data.txt文件中
#     数据如下：
#         小张 13888888888
#         小李 13999999999
#         小赵 13666666666
#     写程序读取数据，打印姓名和电话，格式如下：
#     姓名：小张，电话：13888888888
try:
    file = open('data.txt')
    data_list = file.readlines()
    for d in data_list:
        _ = d.split(' ')
        print('姓名：%s，电话：%s'%(_[0],_[1].rstrip('\n')))
    
except IOError:
    print('无此文件')
finally:
    file.close()