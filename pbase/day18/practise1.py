# 练习： 
#     写一个Bicycle(自行车类)类，有run方法，调用时显示骑行里程km

#     class Bicycle:
#         def run(self,km):
#             print('自行车骑行了',km,'公里')

#     再写一个电动自行车类继承自Bicycle,添加电池电量valume属性，同时有两个方法：
#         1.fill_charge(vol) 用来充电
#         2.run(km) 方法用于骑行，每骑行10km消耗电量1度，当电量耗尽时调用Bicycle的run方法骑行
#         并显示骑行结果
#         主程序：
#             b = EBicycle(5) #创建一个电动自行车，默认电量5度
#             b.run(10)  #骑行10km
#             b.run(100) #骑行100km
#             b.fill_charge(6) #充电6度
#             b.run(70) #又骑行70km

class Bicycle():
    def run(self,km):
        print('自行车骑行了%d公里'%km)

class EBicycle(Bicycle):
    def __init__(self,vol):
        self.vol = vol
    def fill_charge(self,vol):
        self.vol += vol
        print('充了%d度电，还有%d度电'%(vol,self.vol))
    def run(self,km):
        if self.vol - km/10 < 0:
            print('电动自行车自动行驶了%d公里,电量耗尽'%(self.vol * 10))
            super().run(km - self.vol*10) 
            self.vol = 0
        else:
            self.vol -= km/10
            print('电动自行车自动行驶了%d公里,还剩%d度电'%(km,self.vol))
            
b = EBicycle(5) #创建一个电动自行车，默认电量5度
b.run(10)  #骑行10km
b.run(100) #骑行100km
b.fill_charge(6) #充电6度
b.run(70) #又骑行70km
