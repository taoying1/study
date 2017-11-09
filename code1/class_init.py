class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print("Hello, how are you?",self.name)

p=Person('Lily')
p.sayHi()


#__init__方法在类的一个对象被建立时，马上运行。这个方法可以用来对你的对象做一些你希望的初始化 。