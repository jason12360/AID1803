#此示例示意try-finally语句的用法：

#厨房做饭为例：

def fry_egg():
    print('打开天然气')
    try:
        count = int(input('请输入鸡蛋个数:'))
        print('完成煎鸡蛋！共煎了%d个鸡蛋'%count)
    finally:
        print('关闭天然气')

fry_egg()
