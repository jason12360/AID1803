#此示例示意raise语句的用法
def make_except(n):
    #假设n必须是0-100之间的数
    print('begin开始处理')
    if n > 100: #传过来的参数无效，怎么告诉调用着呢
        raise ValueError('您输入的数字大于100')
    print('end')  

try:
    number = int(input('请输入一个整数：'))
    make_except(number)
except ValueError as e:
    print('您输入的数字不符合要求',e)