###########################python inheritence#########################
class Animal:
    def eat(self):
        print("I can eat")
    
    def sleep(self):
        print("I am asleep")
    
#derived class
class Dog(Animal):

    def bark (self):
        print("I can bark")
    
#instance
dogOne = Dog()

#call members of the base class
dogOne.eat()
dogOne.sleep
#call members of the derived class
dogOne.bark()