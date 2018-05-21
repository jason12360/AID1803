#本示例示意实例方法的定义方法和调用
class Dog:
    def eat(self,food):
        print('小狗吃了',food)
    def sleep(self,hour):
        print('小狗睡了',hour,'小时')

dog1 = Dog()
dog1.eat('骨头')
dog1.sleep(1)

dog2 = Dog()
dog2.eat('包子')
dog2.sleep(2)

dog3 = Dog()
Dog.eat(dog3,'狗粮')
Dog.sleep(dog3,3)