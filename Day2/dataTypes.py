#data types

#string
import string


print("Hello"[4])

#integer
print(222 + 444)

#float
3.142

#boolean
True
False

# checking data type
number = len("Hello")

#returns data type
type(number)

#typecasting (changing a data type to another)

new_number = str(number)

print(new_number)

#coding exercise
#add 2 digits in a number

two_digit_number = input("Type a two digit number")

#convert to int since input is received as string
numberOne = int(two_digit_number[0])
numberTwo = int(two_digit_number[1])

print(numberOne + numberTwo)

#number modification

#rounding numbers

#round to 2 decimal places
print(round(2.666666, 2))

#flooring - dividing a number and leaving the result in integer form

print(9 // 2)

#User scores a point

score = 0

score += 1