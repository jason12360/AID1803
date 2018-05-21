  #输入一个成绩，如果成绩在0~100则合法，否则提示”您的输入有误“。

score = int(input('请输入一个成绩'))
if score >= 0 and score <= 100:
    pass
else:
    print('您的输入有误')
