#给定VIP用户，在存取取钱时，判断是否为VIP用户
VIP = ['小张']

def priv_check(fn):
    def privilage(name,x):
        print('正在权限验证')
        if name in VIP:
            fn(name,x)
            print('尊贵的VIP用户',name,'，您已成功完成操作。')
        else:
            print('此处仅供VIP用户使用，您没有权限。')
    return privilage

#以下函数一半固定
@priv_check
def save_money(name,x):
    print(name,'存钱',x,'元')
@priv_check
def withdraw(name,x):
    print(name,'取钱',x,'元')

#以下为开发者调用时

save_money('小张',300)
withdraw('小李',500)
