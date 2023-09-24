#python directory and files management

#get current directory
import os

print(os.getcwd())

#change directory
os.chdir('Users/leesangoroh')

#list directories and files in python

#lists all subdirectories
os.listdir()

os.listdir('Users/leesangoroh')

#make directory
os.mkdir('test')

#rename a directory
os.rename('test','newOne')

#remove directory or file
os.remove('newOne.txt')

#remove directory
os.rmdir('newOne')

# remove dir using the shutil module
import shutil

shutil.rmtree('mydir')

###################python exception handling###########################
#exceptions abnormally terminate the execution of a program
#hence we are supposed to handle these exceptions
try:
    #code that may cause an exception
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    #code to run when exception occurs
    print('Denominator cannot be 0')

#catching specific exceptions in python
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

#python try with else clause
# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

#python try...finally block
#the finally block must be executed no matter whether there is an exception or not
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0")
finally:
    print("This must be executed")

#python custom exceptions
#we can define custom exceptions by creating a new class that is derived from the built-in
#Exception class

#when developing a large python program, its good practice to place all user-defined
#exceptions in a separate file

class InvalidAgeException(Exception):

    pass
number = 18

try:
    inputNum = int(input("Enter a number: "))
    if inputNum < number:
        raise InvalidAgeException
    else:
        print('Eligible to vote')

except InvalidAgeException:
    print('Exception occurred: Invalid Age')


#customizing the exception class


class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)