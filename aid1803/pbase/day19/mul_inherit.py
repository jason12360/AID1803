#此示例示意多继承
class Car:
    def run(self,speed):
        print('汽车以',speed,'km/h的速度行驶')

class Plane:
    def fly(self,height):
        print('飞机以海拔',height,'米高度飞行')

class PlaneCar(Car,Plane):
    """飞行汽车类，是继承自Car和Plane"""
    pass

pc = PlaneCar()
pc.run(100)
pc.fly(10000)