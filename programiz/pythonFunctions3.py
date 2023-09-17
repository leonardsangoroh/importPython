##########################################functions###########################################
#there are standard library functions (built-in functions) & user-defined functions
def greet():
    print("Semaje Sangoroh")

greet()

#function with 2 arguments
def add_numbers(num1,num2):
    sum = num1+num2
    return sum

answer = add_numbers(9,92)
print(answer)

#python library function

import math

#squareRoot
squareRoot = math.sqrt(4)

#power
power = pow(2,3)

#function argument with default values
def summation (a=7,b=3):
    sum = a + b
    print(sum)

#ways of calling summation()
summation(4,48)

summation(48)

summation()

#python keyword argument
def displayNames(fName, lName):
    print(fName, ' ', lName)

#function call - the order of arguments passed doesn't matter
displayNames(lName='Sangoroh',fName='Lee')

#function with arbitrary arguments
def findSum(*numbers):

    result = 0

    for number in numbers:
        result = result + number
    print(result)

# function call with 3 arguments
findSum(1, 2, 3)

# function call with 2 arguments
findSum(4, 9)

####################################python recursion###################################
#recursion is the process of defining something in terms of itself

#every recursive condition must have a base condition

def factorial(X):

    if X == 1:
        return 1
    else:
        return(X * factorial(X-1))


num = 3
print("The factorial of ", num, "is ", factorial(num))

###############################python lambda/ anonymous function##############################
nisalimie = lambda : print("Niaje Sangoroh")

#call the lambda function
nisalimie()

#lambda function with an argument
nisalimieVizuri = lambda name : print("Semaje ", name)

nisalimieVizuri('Lee Leonard Sangoroh')

###############################python variable scope##############################

#local variable
def greet():
    #local variable
    message = 'Hello'
    print(message)

greet()
#when you try to print 'message' variable outside the greet function, it will bring a NameError

#global variable
#declared outside a function or in global scope
message = 'Hello'

def greet():
    #declare local variable
    print('Local ', message)

greet()
print('Global ', message)

#nonlocal variable
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()