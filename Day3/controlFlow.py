from unittest import result


print("Welcome to the Roalercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the roalercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride")

# coding exercise
# check whether the number is odd or even

number = int(input("Which number do you want to check? "))

result = number%2

if result == 1:
    print("odd")

else:
    print("even")