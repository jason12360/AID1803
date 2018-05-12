# #1.BMI值计算
#         BMI = 体重（公斤）/身高（米）平方
#         BMI<18.5     体重过轻
#         18.5<=BMI<24 正常
#         BMI>=24      异常范围
#         如：BMI = 69/1.73*1.73
#         要求输入身高，体重，打印BMI值情况

H = float(input('请输入您的身高'))
W = float(input('请输入您的体重'))
BMI = W / H ** 2
if BMI < 18.5:
    print('您的体重过轻')
elif BMI >= 18.5 and BMI < 24:
    print('您的体重正常')
elif BMI >= 24:
    print('您的体重异常')
