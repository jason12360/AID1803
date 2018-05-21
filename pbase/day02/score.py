#判断一个学生成绩，如果不在0~100之间，就提示：不合法的输入，否则就是啥也不提示
score = int(input('请输入分数'))
if 0 <= score <= 100:
    pass
else:
    print('不合法的输入')