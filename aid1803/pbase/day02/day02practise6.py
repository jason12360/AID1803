# #输入三个学生的成绩，
#         打印出最高分是多少？
#         打印出最低分是多少？
#         打印出平均分是多少？

s1 = float(input('请输入第一个学生的成绩'))
s2 = float(input('请输入第二个学生的成绩'))
s3 = float(input('请输入第三个学生的成绩'))

# max = s1
# if s2 > max:
#     max = s2
# if s3 > max:
#     max = s3

# min = s1
# if s2 < min:
#     min = s2
# if s3 < min:
#     min = s3

# print('最高分是',max)
# print('最低分是',min)
# print('平均分是',(s1 + s2 + s3) / 3)



if s1>s2:
    s1,s2=s2,s1
if s2>s3:
    s2,s3=s3,s2
if s1>s2:
    s1,s2=s2,s1
print('最高分是',s3)
print('最低分是',s1)
print('平均分是',(s1 + s2 + s3) / 3)


