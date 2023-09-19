##################################python numeric data type########################################
numOne = 1
print(type(numOne)) #int

numTwo = 1.34
print(type(numTwo)) #float

numThree = 8 + 2j
print(type(numThree)) #complex

#number systems
print(0b1101011)  # prints 107

print(0xFB + 0b10)  # prints 253

print(0o15)  # prints 13

#explicit type conversion
num1 = int(2.3)
print(num1)  # prints 2

num2 = int(-2.8)
print(num2)  # prints -2

num3 = float(5)
print(num3) # prints 5.0

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)

##################################python random module########################################
import random

#print a random number between 10 and 20
print(random.randrange(10,20))

listOne = ['a','b','c','d','e']

#get a random item from listOne
print(random.choice(listOne))

#shuffle the list
random.shuffle(listOne)
print(listOne)

#print a random element
print(random.random())

##################################python mathematics########################################
import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))

##################################python lists########################################
