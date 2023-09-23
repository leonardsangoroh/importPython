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
