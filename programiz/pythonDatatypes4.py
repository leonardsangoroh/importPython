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

##################################python tuples########################################
#same as list, just that tuples are immutable

#creating a tuple
myTuple = (1, 'Lee', 'Leonard', 'Lee')
print(myTuple)

#accessing elements
print(myTuple[2])

#python tuple methods
print(myTuple.count('Lee')) # counts total number of 'p' in myTuple
print(myTuple.index('Lee')) # returns the first index occurrence of l in myTuple


##################################python strings########################################
#python strings are immutable, meaning characters of a string cannot be changed

#access string characters in python
greet = 'hello'

print(greet[1]) #prints 'e'

#slicing
print(greet[1:4])

#multiline string
message = """
One day you'll leave this world behind,
So live a life you will remember
"""

#string operations

#compare 2 strings
stringOne = 'hello'
stringTwo = 'Helllo'

print(stringOne == stringTwo) #returns False

#join two or more strings
print(stringTwo + stringOne)


#iterate through a python string
for character in stringOne:
    print(character)

#python string length
print(len(stringOne))

#string membership test
print('h' in stringOne) #true

#escape sequence in python
print('Lee said, \"Managu unatoa wapi Nairobi" ')

#f-strings
#easy to print values and variables
name = 'Leonard'
country = 'Kenya'

print(f'{name} is from {country}')

##################################python sets########################################
#a collection of unique data
#sets are mutable
#a set can have any number of items and they may be of different types

#create a set of mixed data types
mixedSet = {'Hello', 101, -2, 'Bye'}
print(mixedSet)

#create an empty set
emptySet = set()

#empty dictionary
emptyDictionary = {}

#add & update items to a set
mixedSet.add(34)

#update - used to update the set with items of other collection types(lists, tuples, sets)
companies = {'Toyota','Mitsubishi','Chevrolet'}

tech_companies = ['Google', 'FaceBook']

companies.update(tech_companies)

print(companies)

#remove elements from a set
companies.discard('Toyota')

#iterate over a set in python
for company in companies:
    print(companies)

#number of sets elements
print(len(companies))

#python set operations

A = {1,3,5}

B = {0,2,4}

#union
print(A|B)

print(A.union(B))

#intersection
print(A & B)

print(A.intersection(B))

#difference btw 2 sets
#what is in A but not in B
print(A - B)
print(A.difference(B))

#set symmetric difference
#in A and B but not in both
print(A ^ B)
print(A.symmetric_difference(B))

#check it two sets are equal
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')


##################################python dictionary########################################
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

print(country_capitals)

#check length
print(len(country_capitals))

#access dictionary items
print(country_capitals["England"])

#change dictionary items
country_capitals["England"] = "Changed"

#add an item
country_capitals["Germany"] = "Berlin"

#remove item
del country_capitals["Germany"]

#remove all items
country_capitals.clear()

#membership test
print('England' not in country_capitals)

#iterating through a dictionary
for capital in country_capitals:
    x = country_capitals[capital]
    print(x)