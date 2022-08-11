#data types

#string
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
