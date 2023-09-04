#Indentifiers - names given to variables, classes, methods etc
language = 'Python'
print(language)

#####################Commenting################################

#Single line comment

#Multiple
#Line
#Comment

"""
Multiple line comment
Used to declare multiple line strings but can be used for comments
if not assigned to a variable
"""

#####################Variables################################

#we use the assignment operator '=' to assign a value
number = 10
print(number)

#changing the value of a variable in python
number = 11
print(number)

#assigning multiple values to multiple variables
a, b, c = 5, 3.2, 'Lee'

#assign same value to multiple variables
programmerOne = programmerTwo = 'Lee'

#python constants

#constant - a special type of variable who's value can't be changed

#Constants are declared and assigned in a modle - a separate file
#containing variables, functions ets which is imported to the main file

import constant

print(constant.PI)

###########variables,constants,literals######################

#python literals - the initial contents of a variable
#used to assign values to variables or constants
#literals - a representation of fixed values in a program
character_literal = 'a'
integer_literal = 42
float_literal = 3.14
string_literal = "Hello, World!"
boolean_literal = True
list_literal = [1, 2, 3]
tuple_literal = (4, 5, 6)
dictionary_literal = {'name': 'Alice', 'age': 30}
set_literal = {1, 2, 3}
complex_literal = 2 + 3j

#used to specify a null variable
none_literal = None

#python data types

#numeric - int, float, complex - holds numeric values
num3 = 1 + 3j
print(type(num3))

#string - str - holds a sequence of characters
name = 'Lee'
#sequence - list, tuple, range - holds collection of items

#lists
languages = ['Swift', 'SQL', 'Python']
print(language[2])

#tuple - same as lists but can't be modified
product = ('Xbox', 500.10)
print(product[0])

#mapping - dict - holds data in key-value pair form
capital_city = {'Kenya':'Nairobi','Uganda':'Kampala', 'Rwanda':'Kigali'}
print(capital_city)
print(capital_city['Kenya'])

#boolean - bool - holds either True or False

#set - set, frozeenset - holds collection of unique items
#set - an unordered collection of unique items
student_id = {134327, 134328, 134329, 134330}
print(student_id)
#Since sets have no defined order, there are no indices to use for slicing.


#####################Type Conversion################################

#implicit conversion
#done sometimes to avoid data loss
numOne = 321
numTwo = 1.44
print('The result is ', numOne+numTwo)
#result = 322.44

#explicit conversion/typecasting
#int()
#float()
#str()

#####################I/O & Import################################
print('Good night')
#output: Good night

# print with end whitespace
print('Good Morning!', end= ' ')

print('It is rainy today')

#output: Good morning! It is rainy today


#print with sep parameter
print('New Year', 2023, 'See you soon!', sep= '. ')

#output: New Year. 2023. See you soon!