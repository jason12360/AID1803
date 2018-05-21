  # 北京出租计价器算法
  #       收费标准
  #       1）3公里以内13元
  #       2）超出3公里以外，每公里基本单价2.3元/公里
  #       3）空驾费：超过15公里后，每公里加收单价50%空驾费
  #       要求输入公里数，打印费用金额（以元为单位四舍五入）

shuru = input('请输入公里数： ')
if shuru.isdigit():
  dis = float(shuru)
  cost = 0 
  if 0 < dis <= 3:
      cost = 13
      print('您的打车费用是',cost,"元")
  elif 3 < dis <= 15:
      cost = 2.3 * (dis - 3) + 13
      print('您的打车费用是',round(cost),"元")
  elif dis > 15:
      cost = 2.3 * 1.5 * (dis - 15) + 2.3 * (15 - 3) + 13
      print('您的打车费用是',round(cost),"元")
  else:
      print('你输入的公里数有误')
else:
  print('你输入的公里数有误')
  