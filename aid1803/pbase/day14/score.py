 # 练习：
 #        写一个函数，get_score()来获取用户输入的学生成绩（0-100）
 #        如果输入出现错误，则此函数返回0，如果用户输入数是1-100之间的数返回这个数

def get_score():
    try:
        score = int(input('请输入学生的成绩: '))
        return range(101)[score]
    except:
        return 0

print('学生的成绩是',get_score())

