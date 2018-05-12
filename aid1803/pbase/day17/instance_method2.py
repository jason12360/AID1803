#本示例示意实例方法的定义方法和调用
class Dog:
    def eat(self,food):
        self.food = food
        print('小狗吃了',food)
    def food_info(self):
        print('上次吃的是',self.food)

dog1 = Dog()
dog1.eat('骨头')
dog1.food_info()

# dog2 = Dog()
# dog2.eat('包子')
# dog2.sleep(2)

# dog3 = Dog()
# Dog.eat(dog3,'狗粮')
# Dog.sleep(dog3,3)