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
#a list can store elements of different data types and also store duplicate elements

listOne = [1, 'Lee', 'Lee']

#accessing list elements
print(listOne[2])

#negative indexing
#the index -1 refers to the last item, -2 refers to the second last item

#slicing a list - getting a portion of a list
print(listOne[0:2]) #get from index 0 to 1
print(listOne[1:])  # from index 1 to the end
print(listOne[:]) #print from beginning to end

#add elements to a list

# .append adds element to the end of the list
numbers = [0,1,2,3]
numbers.append(4)

# .extend adds all items of an iterable
moreNumbers = [34,55,68,22,82]

numbers.extend(moreNumbers)

# .insert adds at a specified index

#insert 30 at index 1
numbers.insert(1,30)


#change list items
numbers[4] = 33

#remove items from a list

#using del statement
del moreNumbers[1]

del moreNumbers[-1]

del moreNumbers[0:2]

#using remove
listOne.remove('Lee')


#iterating through a list
languages = ['Python','Swift','MySQL']

for language in languages:
    print(language)

#check element existence - return True or False
print('English' in languages)

#check length
print(len(languages))


#list comprehension - creating a list
nambari = [n**2 for n in range(1,6)]
print(nambari)

#or

nambariHalisi = []

for n in range(1,6):
    nambariHalisi.append(n**2)