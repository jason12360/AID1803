#商场促销，满100减20
money = int(input('请输入商品金额：'))
pay = money - 20 if money >= 100 else money
print('您需要支付：',pay,'元')