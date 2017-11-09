class Person:
    population=0
    def __init__(self,name):
        self.name=name
        print("(Initializing %s)"%self.name)
        Person.population+=1
    def __del__(self):
        print("%s says bye"%self.name)
        Person.population -= 1
        if Person.population==0:
            print("I am the last one")
        else:
            print("There are still %d people left."%Person.population)
    def sayhi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print("Hi, my name is %s"%self.name)
    def howmany(self):
        '''prints the current population.'''
        if Person.population==1:
            print("I am the only person here.")
        else:
            print("We have %d persons here"%Person.population)
swaroop=Person('Swaroop')
swaroop.sayhi()
swaroop.howmany()

kalam=Person("kalam")
kalam.sayhi()
kalam.howmany()

swaroop.sayhi()
swaroop.howmany()
